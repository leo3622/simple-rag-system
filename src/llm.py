import os

from langchain_ollama import ChatOllama

model = ChatOllama(
    model=os.getenv("OLLAMA_MODEL", "llama3:latest"),
    base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
    temperature=0,
)

def generate_text(prompt: str) -> str:
    response = model.invoke(prompt)
    return response.content
