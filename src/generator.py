from retriever import search_similar_chunks
from llm import generate_text
from schemas import RetrievedChunk

def build_prompt(question: str, chunks: list[RetrievedChunk]) -> str:
    context = "\n\n".join(
        f"Source: {chunk.source} page {chunk.page}\n{chunk.text}"
        for chunk in chunks
    )

    return f"""
Answer the question using only the context below. If the answer is not contained within 
the context, say you don't know. Do not attempt to use any prior knowledge.

Context:
{context}

Question:
{question}

Answer:
""".strip()

def generate_answer(question: str) -> str:
    chunks = search_similar_chunks(question)
    prompt = build_prompt(question, chunks)
    
    return generate_text(prompt)