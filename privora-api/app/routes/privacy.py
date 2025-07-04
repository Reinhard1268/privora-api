from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict
from app.core.utils import pseudonymize_data, delete_data, get_logs

router = APIRouter()

class DataPayload(BaseModel):
    data: Dict[str, str]

@router.post("/pseudonymize")
async def pseudonymize(payload: DataPayload):
    return pseudonymize_data(payload.data)

@router.post("/delete")
async def delete(payload: DataPayload):
    return delete_data(payload.data)

@router.get("/log")
async def log():
    return {"logs": get_logs()}
