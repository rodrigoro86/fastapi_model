from sqlmodel import Field, SQLModel, Relationship

class Banco_Has_Agencia(SQLModel, table=True):
    __tablename__ = "banco_has_agencia"

    
    banco_n_banco: int = Field(foreign_key="banco.n_banco", primary_key=True)
    agencia_n_agencia: int = Field(foreign_key="agencia.n_agencia", primary_key=True)
    banco: "Banco" = Relationship()
    agencia: "Agencia" = Relationship()