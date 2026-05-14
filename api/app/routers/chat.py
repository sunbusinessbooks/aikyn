from fastapi import APIRouter
from app.schemas import ChatRequest
from app.services.orchestrator import detect_route

router = APIRouter()

@router.post("/")
def chat(request: ChatRequest):
    route = detect_route(request.message)
    return {"message": request.message, "mode": request.mode, "route": route, "status": "queued_for_orchestration"}
