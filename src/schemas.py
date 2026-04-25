from pydantic import BaseModel, Field

class RetrievedChunk(BaseModel):
    text: str
    source: str
    page: int | None = None
    score: float
    metadata: dict = Field(default_factory=dict)
