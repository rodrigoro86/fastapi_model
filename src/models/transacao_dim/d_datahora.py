from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime
from typing import List, Optional

class DDatahora(SQLModel, table=True):
    __tablename__ = "d_datahora"

    id_datahora: int = Field(default=None, primary_key=True)
    datahora: datetime
    ano: int
    mes: int
    dia: int
    hora: int
    minuto: int
    segundos: int
    semana_do_ano: Optional[int] = None

    transacoes: List["FTransacao"] = Relationship(back_populates="datahora")
