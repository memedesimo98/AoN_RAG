import requests
from bs4 import BeautifulSoup

BASE_URL = "https://aonprd.com"

def fetch_page(path: str) -> str:
    """Scarica una pagina da aonprd.com e restituisce il testo pulito."""
    url = f"{BASE_URL}/{path}"
    print(f"Fetching: {url}")

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Rimuove script, stile e menu laterali
    for tag in soup(["script", "style", "nav", "header", "footer"]):
        tag.decompose()

    text = soup.get_text(separator="\n")
    cleaned = "\n".join(line.strip() for line in text.splitlines() if line.strip())

    return cleaned


if __name__ == "__main__":
    try:
        content = fetch_page("RacesDisplay.aspx?ItemName=Human")
        print(content[:2000])
    except Exception as e:
        print("Errore:", e)
