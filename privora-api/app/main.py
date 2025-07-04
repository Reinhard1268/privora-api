from fastapi import FastAPI
from app.routes import privacy

app = FastAPI(title="Privora API", version="0.1")

app.include_router(privacy.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}