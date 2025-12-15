from fastapi import FastAPI
app = FastAPI()

from app.api.endpoints.ingest_data import ingest_router
from app.api.endpoints.get_data import get_router

# Registra os endpoints
app.include_router(ingest_router)
app.include_router(get_router)