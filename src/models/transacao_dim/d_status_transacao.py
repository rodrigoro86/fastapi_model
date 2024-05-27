from sqlmodel import Field, SQLModel, Relationship
from typing import List

class DStatusTransacao(SQLModel, table=True):
    __tablename__ = "d_status_transacao"

    id_status_transacao: int = Field(default=None, primary_key=True)
    status_transacao: str = Field(max_length=45)

    transacoes: List["FTransacao"] = Relationship(back_populates="status_transacao")
