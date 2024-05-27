from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional

class Chave_Pix(SQLModel, table=True):
    __tablename__ = "chave_pix"
    

    chave_pix: int = Field(primary_key=True)
    contas: Optional[List["Conta"]] = Relationship(back_populates="chave_pix")