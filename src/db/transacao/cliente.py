from sqlmodel import SQLModel, Field, create_engine, Session
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession as SAAsyncSession
from sqlalchemy.future import select
import asyncio

from src.models.transacao_teste.cliente import Cliente


# Configuração do banco de dados assíncrono
DATABASE_URL = "sqlite+aiosqlite:///./db/db_transacao_teste.db"
engine = create_async_engine(DATABASE_URL, echo=False)

# Função para criar as tabelas
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

# Classe para gerenciar inserção de clientes
class Cliente_DB:
    def __init__(self):
        self.engine = engine

    async def create_cliente(self, cliente: Cliente):
        cliente = Cliente.from_orm(cliente)
        async with AsyncSession(self.engine) as session:
            try:
                session.add(cliente)
                await session.commit()
                await session.refresh(cliente)
                return True
            except Exception as e:
                return False

        
       


