import os
import re
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://aonprd.com"

# -------------------------------
# Utility
# -------------------------------

def fetch_html(path: str) -> BeautifulSoup:
    url = f"{BASE_URL}/{path}"
    print(f"Fetching: {url}")
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")

def sanitize_filename(name: str) -> str:
    # Rimuove caratteri illegali per Windows
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    # Rimuove spazi iniziali/finali
    name = name.strip()
    return name

# -------------------------------
# Estrazione categorie
# -------------------------------

def extract_category_links() -> list:
    """Estrae TUTTI i link alle categorie dei talenti, inclusi quelli con spazi, # o vuoti."""
    soup = fetch_html("Feats.aspx")
    links = []

    for a in soup.find_all("a"):
        href = a.get("href", "")

        # tutte le categorie iniziano così
        if href.startswith("Feats.aspx?Category="):
            links.append(href)

    return links

# -------------------------------
# Estrazione talenti da categoria
# -------------------------------

def extract_feat_links(category_path: str) -> dict:
    """Estrae i link ai talenti da una categoria."""
    soup = fetch_html(category_path)
    feats = {}

    for a in soup.find_all("a"):
        href = a.get("href", "")

        # pattern corretto per i talenti
        if href.startswith("FeatDisplay.aspx?ItemName="):
            name = a.text.strip()
            if name:
                feats[name] = href

    return feats

# -------------------------------
# Salvataggio talento
# -------------------------------

def save_feat(name: str, path: str):
    soup = fetch_html(path)

    # pulizia HTML
    for tag in soup(["script", "style", "nav", "header", "footer"]):
        tag.decompose()

    text = soup.get_text(separator="\n")
    cleaned = "\n".join(line.strip() for line in text.splitlines() if line.strip())

    os.makedirs("data/feats", exist_ok=True)

    safe_name = sanitize_filename(name)
    filename = f"data/feats/{safe_name}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(cleaned)

    print(f"Saved: {filename}")

# -------------------------------
# Main
# -------------------------------

if __name__ == "__main__":
    categories = extract_category_links()
    print(f"Trovate {len(categories)} categorie di talenti.")

    all_feats = {}

    for cat in categories:
        feats = extract_feat_links(cat)
        print(f"Categoria {cat}: trovati {len(feats)} talenti.")
        all_feats.update(feats)

    print(f"Totale talenti trovati: {len(all_feats)}")

    for name, path in all_feats.items():
        save_feat(name, path)
