import os
from uuid import uuid5, NAMESPACE_URL

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams

COLLECTION_NAME = "rag_chunks"
VECTOR_SIZE = 384  # all-MiniLM-L6-v2 embedding size
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")


client = QdrantClient(url=QDRANT_URL)


def create_collection() -> None:
    if client.collection_exists(COLLECTION_NAME):
        return

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=VECTOR_SIZE,
            distance=Distance.COSINE,
        ),
    )


def save_chunks(chunks, embeddings: list[list[float]]) -> None:
    points = []

    for index, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        source = chunk.metadata.get("source", "unknown")
        page = chunk.metadata.get("page", 0)

        point_id = str(uuid5(NAMESPACE_URL, f"{source}:page:{page}:chunk:{index}"))

        points.append(
            PointStruct(
                id=point_id,
                vector=embedding,
                payload={
                    "text": chunk.page_content,
                    "source": source,
                    "page": page,
                    "metadata": chunk.metadata,
                },
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points,
        wait=True,
    )
