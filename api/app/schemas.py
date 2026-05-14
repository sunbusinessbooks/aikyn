from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    mode: str = "auto"

class IngestRequest(BaseModel):
    source: str
    source_type: str = "pdf"
