from sqlmodel import Field, SQLModel, Relationship
from typing import List

class DTipoTransacao(SQLModel, table=True):
    __tablename__ = "d_tipo_transacao"

    
    id_tipo_transacao: int = Field(default=None, primary_key=True)
    tipo_transacao: str = Field(max_length=45)

    transacoes: List["FTransacao"] = Relationship(back_populates="tipo_transacao")
