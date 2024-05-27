from sqlmodel import Field, SQLModel, Relationship
from typing import List

class Status_Transacao(SQLModel, table=True):
    __tablename__ = "status_transacao"
    

    id_status_transacao: int = Field(primary_key=True)
    nome_status_transacao: str = Field(max_length=45)
    transacoes: List["Transacao"] = Relationship(back_populates="status_transacao")