from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime
from decimal import Decimal
from typing import Optional

class Transacao(SQLModel, table=True):
    __tablename__ = "transacao"
    

    id_transacao: int = Field(primary_key=True)
    n_conta_origem: int = Field(foreign_key="conta.n_conta")
    n_conta_destino: int = Field(foreign_key="conta.n_conta")
    movimento_id_movimento: int = Field(foreign_key="movimento.id_movimento")
    data_liquidacao: Optional[datetime] = Field(default=None)
    data_transacao: datetime
    id_status_transacao: int = Field(foreign_key="status_transacao.id_status_transacao")
    valor_transacao: Decimal
    CPFCNPJ_credor: int
    CPFCNPJ_pagador: int
    conta_origem: "Conta" = Relationship(back_populates="transacao_conta_origem")
    conta_destino: "Conta" = Relationship(back_populates="transacao_conta_destino")
    movimento: "Movimento" = Relationship(back_populates="transacao_movimento")
    status_transacao: "Status_Transacao" = Relationship(back_populates="transacao_status_transacao")