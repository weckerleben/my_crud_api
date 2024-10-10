from fastapi import FastAPI
from src.interfaces.api.item_routes import router as item_router
from src.infrastructure.database import init_db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(item_router, prefix="/api")
