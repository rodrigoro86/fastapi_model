from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional
from datetime import datetime

class DClientes(SQLModel, table=True):
    __tablename__ = "d_clientes"
    

    cpfcnpj: int = Field(default=None, primary_key=True)
    nome: str = Field(max_length=45)
    sobrenome: Optional[str] = Field(max_length=45, default=None)
    razao_social: Optional[str] = Field(max_length=45, default=None)
    rg: Optional[str] = Field(max_length=45, default=None)
    data_nasc: Optional[datetime] = Field(default=None)
    sexo: Optional[str] = Field(max_length=45, default=None)
    tel_contato: Optional[int] = Field(default=None)

    transacoes_pagador: List["FTransacao"] = Relationship(back_populates="cliente_pagador", sa_relationship_kwargs={"foreign_keys": "[FTransacao.cpfcnpj_pagador]"})
    transacoes_credor: List["FTransacao"] = Relationship(back_populates="cliente_credor", sa_relationship_kwargs={"foreign_keys": "[FTransacao.cpfcnpj_credor]"})
