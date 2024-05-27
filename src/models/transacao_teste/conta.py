from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional
from decimal import Decimal

class Conta(SQLModel, table=True):
    __tablename__ = "conta"


    n_conta: int = Field(primary_key=True)
    clientes_CPF_CNPJ: int = Field(foreign_key="cliente.CPF_CNPJ")
    saldo: Decimal
    cliente: "Cliente" = Relationship(back_populates="contas")
