from sqlmodel import Field, SQLModel, Relationship
from typing import List

class Banco(SQLModel, table=True):
    __tablename__ = "banco"

    
    n_banco: int = Field(primary_key=True)
    nome_banco: str = Field(max_length=45)
    agencias: List["Agencia"] = Relationship(back_populates="banco")