from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime
from typing import Optional

class FTransacao(SQLModel, table=True):
    __tablename__ = "f_transacao"


    id_transacao: int = Field(default=None, primary_key=True)
    n_banco_pagador: int = Field(foreign_key="d_banco.n_banco")
    n_agencia_pagador: int = Field(foreign_key="d_agencia.n_agencia")
    n_conta_pagador: int
    cpfcnpj_pagador: int = Field(foreign_key="d_clientes.cpfcnpj")
    chave_pix_pagador: Optional[str] = Field(max_length=45, default=None)
    n_banco_credor: int = Field(foreign_key="d_banco.n_banco")
    n_agencia_credor: int = Field(foreign_key="d_agencia.n_agencia")
    n_conta_credor: int
    cpfcnpj_credor: int = Field(foreign_key="d_clientes.cpfcnpj")
    chave_pix_credor: Optional[str] = Field(max_length=45, default=None)
    valor_transacao: int
    data_transacao: datetime
    id_status_transacao: int = Field(foreign_key="d_status_transacao.id_status_transacao")
    id_tipo_transacao: int = Field(foreign_key="d_tipo_transacao.id_tipo_transacao")
    data_liquidada: Optional[datetime] = Field(default=None)

    datahora: "DDatahora" = Relationship(back_populates="transacao_datahora")
    tipo_transacao: "DTipoTransacao" = Relationship(back_populates="transacao_tipo_transacao")
    status_transacao: "DStatusTransacao" = Relationship(back_populates="transacao_status")
    cliente_pagador: "DClientes" = Relationship(back_populates="transacao_pagador")
    cliente_credor: "DClientes" = Relationship(back_populates="transacao_credor")
    banco_pagador: "DBanco" = Relationship(back_populates="transacao_pagador")
    banco_credor: "DBanco" = Relationship(back_populates="transacao_credor")
    agencia_pagador: "DAgencia" = Relationship(back_populates="transacao_pagador")
    agencia_credor: "DAgencia" = Relationship(back_populates="transacao_credor")
