from sqlmodel import Field, SQLModel, Relationship
from typing import List

class DBanco(SQLModel, table=True):
    __tablename__ = "d_banco"
    

    n_banco: int = Field(default=None, primary_key=True)
    nome_banco: str = Field(max_length=45)

    agencias: List["DAgencia"] = Relationship(back_populates="banco")
    transacoes_pagador: List["FTransacao"] = Relationship(back_populates="banco_pagador", sa_relationship_kwargs={"foreign_keys": "[FTransacao.n_banco_pagador]"})
    transacoes_credor: List["FTransacao"] = Relationship(back_populates="banco_credor", sa_relationship_kwargs={"foreign_keys": "[FTransacao.n_banco_credor]"})
