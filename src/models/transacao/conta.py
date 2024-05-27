from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional
from decimal import Decimal

class Conta(SQLModel, table=True):
    __tablename__ = "conta"


    n_conta: int = Field(primary_key=True)
    clientes_CPF_CNPJ: int = Field(foreign_key="cliente.CPF_CNPJ")
    chave_pix_chave_pix: Optional[int] = Field(default=None, foreign_key="chave_pix.chave_pix")
    saldo: Decimal
    #cliente: "Cliente" = Relationship(back_populates="contas")
    chave_pix: Optional["Chave_Pix"] = Relationship(back_populates="contas")
    transacoes: List["Transacao"] = Relationship(back_populates="conta_transacao")