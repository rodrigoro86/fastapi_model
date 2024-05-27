from sqlmodel import Field, SQLModel, Relationship
from typing import List

class Agencia(SQLModel, table=True):
    __tablename__ = "agencia"

    n_agencia: int = Field(primary_key=True)
    banco_n_banco: int = Field(foreign_key="banco.n_banco")
    banco: "Banco" = Relationship(back_populates="agencias")
    contas: List["Conta"] = Relationship(back_populates="agencia")