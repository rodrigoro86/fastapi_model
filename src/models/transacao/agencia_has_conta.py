from sqlmodel import Field, SQLModel, Relationship

class Agencia_Has_Conta(SQLModel, table=True):
    __tablename__ = "agencia_has_conta"
    

    agencia_n_agencia: int = Field(foreign_key="agencia.n_agencia", primary_key=True)
    conta_n_conta: int = Field(foreign_key="conta.n_conta", primary_key=True)
    conta_clientes_CPFCNPJ: int = Field(foreign_key="cliente.CPF_CNPJ")
    agencia: "Agencia" = Relationship()
    conta: "Conta" = Relationship()