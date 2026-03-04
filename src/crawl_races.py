import os
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://aonprd.com"

def fetch_html(path: str) -> BeautifulSoup:
    url = f"{BASE_URL}/{path}"
    print(f"Fetching: {url}")
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")

def extract_category_links() -> list:
    """Estrae i link alle categorie Core e Other."""
    soup = fetch_html("Races.aspx")
    links = []

    for a in soup.find_all("a"):
        href = a.get("href", "")
        if "Races.aspx?Category=" in href:
            links.append(href)

    return links

def extract_race_links(category_path: str) -> dict:
    """Estrae i link alle razze da una categoria."""
    soup = fetch_html(category_path)
    races = {}

    for a in soup.find_all("a"):
        href = a.get("href", "")
        if "RacesDisplay.aspx?ItemName=" in href:
            name = a.text.strip()
            races[name] = href

    return races

def save_race(name: str, path: str):
    soup = fetch_html(path)

    for tag in soup(["script", "style", "nav", "header", "footer"]):
        tag.decompose()

    text = soup.get_text(separator="\n")
    cleaned = "\n".join(line.strip() for line in text.splitlines() if line.strip())

    os.makedirs("data/races", exist_ok=True)
    filename = f"data/races/{name}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(cleaned)

    print(f"Saved: {filename}")

if __name__ == "__main__":
    categories = extract_category_links()
    print(f"Trovate {len(categories)} categorie.")

    all_races = {}

    for cat in categories:
        races = extract_race_links(cat)
        print(f"Categoria {cat}: trovate {len(races)} razze.")
        all_races.update(races)

    print(f"Totale razze trovate: {len(all_races)}")

    for name, path in all_races.items():
        save_race(name, path)
