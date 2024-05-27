from sqlmodel import Field, SQLModel, Relationship
from typing import List

class DCep(SQLModel, table=True):
    __tablename__ = "d_cep"

    cep: int = Field(default=None, primary_key=True)
    rua: str = Field(max_length=45)
    bairro: str = Field(max_length=45)

    clientes: List["DClientes"] = Relationship(back_populates="cep")
