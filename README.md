# Simple RAG System

A local retrieval-augmented generation project for indexing PDF documents and searching them with semantic similarity.

The project loads PDFs from `data/raw`, splits them into chunks, creates embeddings with `sentence-transformers/all-MiniLM-L6-v2`, stores vectors in Qdrant, and retrieves the most relevant chunks for a user query. It also includes an Ollama-backed generator module for answering questions from retrieved context.

## Features

- PDF ingestion from a local folder
- Token-aware document chunking with overlap
- Local Hugging Face sentence-transformer embeddings
- Qdrant vector storage
- CLI query flow for retrieving relevant chunks
- Optional Ollama LLM integration for answer generation

## Project Structure

```text
.
├── src/
│   ├── app.py            # CLI retrieval entry point
│   ├── index.py          # PDF indexing pipeline
│   ├── ingest.py         # PDF loading
│   ├── chunking.py       # Text chunking
│   ├── embeddings.py     # Embedding model helpers
│   ├── vector_store.py   # Qdrant collection and upsert logic
│   ├── retriever.py      # Similarity search
│   ├── generator.py      # RAG prompt and answer generation
│   ├── llm.py            # Ollama model client
│   └── schemas.py        # Shared data models
├── data/raw/             # Local PDFs
├── qdrant_storage/       # Local Qdrant data
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## Requirements

- Python 3.10+
- Docker and Docker Compose, recommended for Qdrant
- Ollama, optional, only needed for generated answers

## Local Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start Qdrant:

```bash
docker compose up -d qdrant
```

Add PDF files to:

```text
data/raw/
```

Index the PDFs:

```bash
python3 src/index.py
```

Run the retrieval CLI:

```bash
python3 src/app.py
```

## Docker Setup

The Compose file starts Qdrant and the app container:

```bash
docker compose up --build
```

The app container mounts:

- `./data` to `/app/data`
- `./hf_cache` to `/app/.cache/huggingface`
- `./qdrant_storage` to Qdrant storage

## Ollama Setup

The default model is `llama3:latest`. Install and run Ollama locally, then pull the model:

```bash
ollama pull llama3
```

For local Python runs, the default Ollama URL is:

```text
http://localhost:11434
```

For Docker Compose runs, the app uses:

```text
http://host.docker.internal:11434
```

You can override the model with:

```bash
export OLLAMA_MODEL=llama3:latest
```

## Environment Variables

| Variable | Default | Description |
| --- | --- | --- |
| `QDRANT_URL` | `http://localhost:6333` | Qdrant endpoint for local Python runs |
| `OLLAMA_BASE_URL` | `http://localhost:11434` | Ollama API endpoint |
| `OLLAMA_MODEL` | `llama3:latest` | Ollama model used by `src/llm.py` |
| `HF_HOME` | unset | Optional Hugging Face cache location |

## Data and Privacy Notes

The following paths are intentionally ignored by git:

- `data/`
- `qdrant_storage/`
- `hf_cache/`
- `.venv/`
- `.env` and `.env.*`
- `__pycache__/` and `*.pyc`

Do not commit PDFs, vector database files, model caches, or environment files unless you have reviewed them and intend to publish them.

## Typical Workflow

1. Put PDFs in `data/raw/`.
2. Start Qdrant with `docker compose up -d qdrant`.
3. Run `python3 src/index.py`.
4. Run `python3 src/app.py`.
5. Enter a question and review the retrieved chunks.
