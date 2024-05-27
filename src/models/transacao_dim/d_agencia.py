from sqlmodel import Field, SQLModel, Relationship
from typing import List

class DAgencia(SQLModel, table=True):
    __tablename__ = "d_agencia"

    n_agencia: int = Field(default=None, primary_key=True)
    n_banco: int = Field(default=None, foreign_key="d_banco.n_banco")

    banco: "DBanco" = Relationship(back_populates="agencias")
    transacoes_pagador: List["FTransacao"] = Relationship(back_populates="agencia_pagador", sa_relationship_kwargs={"foreign_keys": "[FTransacao.n_agencia_pagador]"})
    transacoes_credor: List["FTransacao"] = Relationship(back_populates="agencia_credor", sa_relationship_kwargs={"foreign_keys": "[FTransacao.n_agencia_credor]"})
