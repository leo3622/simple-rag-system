from ingest import load_documents
from chunking import chunk_text
from embeddings import create_embeddings
from vector_store import create_collection, save_chunks


def main() -> None:
    documents = load_documents("data/raw")

    chunks = chunk_text(documents)

    embeddings = create_embeddings([chunk.page_content for chunk in chunks])
    
    create_collection()
    save_chunks(chunks, embeddings)

    print(f"Indexed {len(chunks)} chunks from {len(documents)} document pages")


if __name__ == "__main__":
    main()
