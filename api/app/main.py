from fastapi import FastAPI
from app.routers.health import router as health_router
from app.routers.chat import router as chat_router
from app.routers.ingest import router as ingest_router
from app.routers.search import router as search_router

app = FastAPI(title="AIkyn Core API", version="0.1.0")

app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(chat_router, prefix="/chat", tags=["chat"])
app.include_router(ingest_router, prefix="/ingest", tags=["ingest"])
app.include_router(search_router, prefix="/search", tags=["search"])
