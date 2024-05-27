from fastapi.responses import FileResponse, JSONResponse
from src.models.transacao_teste.cliente import ClienteCreate, Cliente
from src.db.transacao.cliente import Cliente_DB


from fastapi import(
    APIRouter,
)


router = APIRouter()
@router.post("/cliente_create")
async def cliente_create(cliente: ClienteCreate):

    db_cliente = Cliente_DB()
    if await db_cliente.create_cliente(cliente):
        return JSONResponse(content={"message": "Cliente criado com sucesso"})
    else:
        return JSONResponse(content={"message": "Erro ao criar cliente"})
