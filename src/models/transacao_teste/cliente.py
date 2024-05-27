from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional
from pydantic import BaseModel, validator, Field as PydanticField
import re


class ClienteBase(SQLModel):
    CPF_CNPJ: int = PydanticField(..., description="CPF ou CNPJ do cliente", example=12345678901)
    nome: str = PydanticField(..., max_length=45, description="Nome completo do cliente", example="João Silva")
    CEP: int = PydanticField(..., description="Código postal do cliente", example=12345678)
    usuario: str = PydanticField(..., max_length=45, description="Nome de usuário do cliente", example="joaosilva")
    senha: str = PydanticField(..., max_length=45, description="Senha do cliente", example="senha123")
    senha_eletronica: str = PydanticField(..., max_length=45, description="Senha eletrônica do cliente", example="senhaEletronica456")

    @validator('CPF_CNPJ')
    def cpf_cnpj_validator(cls, value):

        if not len(str(value)) > 11:
            value = str(value).zfill(11)
            
        if not isinstance(value, str) or len(str(value)) not in (11, 14):
            raise ValueError('CPF_CNPJ deve ter 11 dígitos para CPF ou 14 dígitos para CNPJ')
        if len(str(value)) == 11:
            if not cls.valida_cpf(str(value)):
                raise ValueError('CPF inválido')
        elif len(str(value)) == 14:
            if not cls.valida_cnpj(str(value)):
                raise ValueError('CNPJ inválido')
        return value

    @staticmethod
    def valida_cpf(cpf: str) -> bool:
        # Função simples para validação de CPF
        cpf = re.sub(r'\D', '', cpf)
        if len(cpf) != 11 or len(set(cpf)) == 1:
            return False
        for i in range(9, 11):
            val = sum((int(cpf[num]) * (i + 1 - num) for num in range(0, i)))
            dig = ((val * 10) % 11) % 10
            if dig != int(cpf[i]):
                return False
        return True

    @staticmethod
    def valida_cnpj(cnpj: str) -> bool:
        # Função simples para validação de CNPJ
        cnpj = re.sub(r'\D', '', cnpj)
        if len(cnpj) != 14 or len(set(cnpj)) == 1:
            return False
        t = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        for i in range(12, 14):
            d = sum(int(cnpj[j]) * t[j + 1 - i] for j in range(i))
            d = ((d * 10) % 11) % 10
            if d != int(cnpj[i]):
                return False
        return True

class Cliente(ClienteBase, table=True):
    __tablename__ = "cliente"
    id_cliente: Optional[int] = Field(default=None, primary_key=True, unique=True, index=True)
    CPF_CNPJ: int = Field(sa_column_kwargs={"unique": True})
    contas: Optional[List["Conta"]] = Relationship(back_populates="cliente")


class ClienteCreate(ClienteBase):
    pass