from embeddings import create_query_embedding
from vector_store import COLLECTION_NAME, client
from schemas import RetrievedChunk
    


def search_similar_chunks(query: str, limit: int = 5) -> list[RetrievedChunk]:
    """Search Qdrant for chunks that are semantically similar to a query."""
    query_embedding = create_query_embedding(query)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_embedding,
        limit=limit,
        with_payload=True,
    ).points

    return [
        RetrievedChunk(
            score=result.score,
            text=result.payload.get("text", ""),
            source=result.payload.get("source", ""),
            page=result.payload.get("page"),
            metadata=result.payload.get("metadata", {}),
        )
        for result in results
    ]
