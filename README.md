AoN_RAG — Retrieval-Augmented Generation su Archive of Nethys (Pathfinder 1e)
AoN_RAG è un progetto sperimentale che costruisce un sistema RAG (Retrieval-Augmented Generation) basato sui contenuti di Archive of Nethys (Pathfinder 1e).
Il sistema esegue scraping delle pagine, genera embedding, costruisce un indice vettoriale FAISS e fornisce risposte contestuali tramite un modello LLM (Gemini 2.0 Flash).

L’obiettivo è permettere interrogazioni naturali su talenti, razze, classi e altre informazioni del regolamento Pathfinder, con risposte accurate e supportate da fonti.

✨ Funzionalità principali
Web scraping modulare di Archive of Nethys (feat, razze, classi, ecc.)

Parsing robusto con gestione delle variazioni strutturali delle pagine

Pulizia e normalizzazione del testo

Chunking dinamico per ottimizzare la qualità degli embedding

Generazione embedding tramite Gemini 2.0 Flash

Indicizzazione vettoriale con FAISS

Pipeline RAG completa: retrieval + generazione risposta

Struttura del progetto pulita e riproducibile

Compatibile con Python 3.11

📁 Struttura del progetto
aon_rag/
│
├── src/
│   ├── fetch/
│   │   ├── fetch_feats.py
│   │   ├── fetch_races.py
│   │   └── ...
│   ├── processing/
│   │   ├── clean_text.py
│   │   ├── chunker.py
│   │   └── ...
│   ├── embeddings/
│   │   ├── embedder.py
│   │   └── ...
│   ├── index/
│   │   ├── build_faiss.py
│   │   └── search_faiss.py
│   └── rag/
│       ├── pipeline.py
│       └── ...
│
├── data/
│   ├── raw/        # HTML o JSON grezzi
│   ├── cleaned/    # Testo pulito
│   ├── chunks/     # Chunk per embedding
│   ├── embeddings/ # Vettori
│   └── index/      # Indice FAISS
│
├── .gitignore
├── requirements.txt
└── README.md

🚀 Installazione
1. Clona il repository

git clone https://github.com/memedesimo98/AoN_RAG.git
cd AoN_RAG

2. Crea un ambiente virtuale

python -m venv .venv
.venv\Scripts\activate

3. Installa le dipendenze

pip install -r requirements.txt

4. Imposta la tua API key di Google AI Studio

GOOGLE_API_KEY=la_tua_api_key

🕸️ Scraping dei contenuti
Esegui gli script di scraping per raccogliere i dati:

python src/fetch/fetch_feats.py
python src/fetch/fetch_races.py

I dati verranno salvati in data/raw/.

🧹 Pulizia e chunking

python src/processing/clean_text.py
python src/processing/chunker.py

🧠 Generazione embedding

python src/embeddings/embedder.py

📦 Costruzione dell’indice FAISS

python src/index/build_faiss.py

🔍 Query RAG
Una volta costruito l’indice:

python src/rag/pipeline.py

Esempio di query:

"Quali talenti migliorano la capacità di lanciare incantesimi in movimento?"

🛠️ Tecnologie utilizzate
Python 3.11

BeautifulSoup4 per scraping

FAISS per indicizzazione vettoriale

Gemini 2.0 Flash per embedding e generazione

dotenv per gestione variabili ambiente

Requests per HTTP client

📌 Note
Il progetto è pensato per uso personale e sperimentale.

Archive of Nethys è un sito di terze parti: rispettare sempre i loro termini d’uso.

Il sistema non sostituisce le regole ufficiali di Pathfinder.

📄 Licenza
MIT License.
