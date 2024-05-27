from sqlmodel import Field, SQLModel, Relationship
from typing import List

class Movimento(SQLModel, table=True):
    __tablename__ = "movimento"
    

    id_movimento: int = Field(primary_key=True)
    nome_movimento: str = Field(max_length=45)
    transacoes: List["Transacao"] = Relationship(back_populates="movimento")