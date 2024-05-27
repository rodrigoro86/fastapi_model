from sqlmodel import Field, SQLModel, Relationship
from typing import List

class Cliente(SQLModel, table=True):
    __tablename__ = "cliente"
    

    CPF_CNPJ: int = Field(primary_key=True)
    nome: str = Field(max_length=45)
    CEP: int
    usuario: str = Field(max_length=45)
    senha: str = Field(max_length=45)
    senha_eletronica: str = Field(max_length=45)
    #contas: List["Conta"] = Relationship(back_populates="cliente")