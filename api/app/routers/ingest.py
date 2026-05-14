from fastapi import APIRouter
from app.schemas import IngestRequest

router = APIRouter()

@router.post("/")
def ingest(request: IngestRequest):
    return {"status": "accepted", "source": request.source, "source_type": request.source_type}
