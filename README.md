AoN_RAG: Pathfinder 1e AI Assistant
AoN_RAG è un sistema di Retrieval-Augmented Generation (RAG) sperimentale e molto basico progettato per interrogare in linguaggio naturale il database di Archive of Nethys (Pathfinder 1st Edition).

Il progetto utilizza Gemini 2.5 Flash per l'elaborazione del linguaggio e la generazione di embedding, permettendo di ottenere risposte precise, contestualizzate e basate sulle regole ufficiali del gioco.

Caratteristiche Principali
Scraping Modulare: Estrazione automatizzata di talenti, razze da Archive of Nethys.

Potenza di Gemini 2.5 Flash: Sfrutta l'ultima versione del modello di Google per un ragionamento superiore e una finestra di contesto estesa.

Ricerca Vettoriale con FAISS: Indicizzazione e recupero dei dati ultra-rapido tramite similarità semantica.

Preprocessing Avanzato: Pulizia del testo e chunking dinamico per massimizzare la pertinenza delle risposte.

Pipeline RAG Completa: Sistema integrato che va dal recupero del documento alla generazione della risposta finale.

Stack Tecnologico
Python 3.11+

Google Gemini 2.5 Flash (API)

FAISS (Facebook AI Similarity Search)

BeautifulSoup4

Python-dotenv

Struttura del Progetto
aon_rag/
├── src/
│   ├── fetch/          # Script per lo scraping dei dati
│   ├── processing/     # Pulizia e segmentazione del testo (chunking)
│   ├── embeddings/     # Generazione vettoriale con Gemini 2.5
│   ├── index/          # Creazione e ricerca su indice FAISS
│   └── rag/            # Pipeline finale di generazione
├── data/
│   ├── raw/            # HTML/JSON originali
│   ├── cleaned/        # Testo normalizzato
│   ├── chunks/         # Segmenti per embedding
│   └── index/          # Database vettoriale salvato
├── requirements.txt
└── README.md
Installazione
Clona il repository:

Bash
git clone https://github.com/memedesimo98/AoN_RAG.git
cd AoN_RAG
Crea e attiva un ambiente virtuale:

Bash
python -m venv .venv
# Su Windows:
.venv\Scripts\activate
# Su Linux/Mac:
source .venv/bin/activate
Installa le dipendenze:

Bash
pip install -r requirements.txt
Configura la tua API Key:
Crea un file .env nella cartella principale e aggiungi:

Snippet di codice
GOOGLE_API_KEY=la_tua_api_key_qui
Utilizzo
Per inizializzare il sistema, esegui gli script nell'ordine seguente:

Raccogli i dati:
python src/fetch/fetch_feats.py (e altri script fetch)

Elabora il testo:
python src/processing/clean_text.py
python src/processing/chunker.py

Genera gli embedding e l'indice:
python src/embeddings/embedder.py
python src/index/build_faiss.py

Avvia le interrogazioni:
python src/rag/pipeline.py

Note Legali
Il progetto è a scopo puramente educativo e sperimentale.

I contenuti estratti appartengono ai rispettivi proprietari e a Archive of Nethys. Si prega di utilizzare il sistema nel rispetto dei loro termini di servizio.

I modelli IA possono generare errori: confronta sempre i risultati con i manuali ufficiali.

Sviluppato da memedesimo98
