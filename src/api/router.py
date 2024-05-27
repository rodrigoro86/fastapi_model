from fastapi import APIRouter
from src.api.transacao import cliente


api_router = APIRouter()

api_router.include_router(cliente.router, prefix='/cliente', tags=['cliente'])
