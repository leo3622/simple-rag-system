from langchain_huggingface import HuggingFaceEmbeddings

embeddings_model_name = "sentence-transformers/all-MiniLM-L6-v2"

embedding_model = HuggingFaceEmbeddings(model_name=embeddings_model_name, 
                                        encode_kwargs={"normalize_embeddings": True},)

def create_embeddings(chunks: list[str]) -> list[list[float]]:
    return embedding_model.embed_documents(chunks)


def create_query_embedding(query: str) -> list[float]:
    """Embed a user query with the same model used for stored chunks."""
    return embedding_model.embed_query(query)
