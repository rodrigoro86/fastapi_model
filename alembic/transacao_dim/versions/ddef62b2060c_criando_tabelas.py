"""Criando Tabelas

Revision ID: ddef62b2060c
Revises: 
Create Date: 2024-05-26 22:36:58.650320

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'ddef62b2060c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('d_banco',
    sa.Column('n_banco', sa.Integer(), nullable=False),
    sa.Column('nome_banco', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('n_banco')
    )
    op.create_table('d_cep',
    sa.Column('cep', sa.Integer(), nullable=False),
    sa.Column('rua', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('bairro', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('cep')
    )
    op.create_table('d_clientes',
    sa.Column('cpfcnpj', sa.Integer(), nullable=False),
    sa.Column('nome', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('sobrenome', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('razao_social', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('rg', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('data_nasc', sa.DateTime(), nullable=True),
    sa.Column('sexo', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('tel_contato', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('cpfcnpj')
    )
    op.create_table('d_datahora',
    sa.Column('id_datahora', sa.Integer(), nullable=False),
    sa.Column('datahora', sa.DateTime(), nullable=False),
    sa.Column('ano', sa.Integer(), nullable=False),
    sa.Column('mes', sa.Integer(), nullable=False),
    sa.Column('dia', sa.Integer(), nullable=False),
    sa.Column('hora', sa.Integer(), nullable=False),
    sa.Column('minuto', sa.Integer(), nullable=False),
    sa.Column('segundos', sa.Integer(), nullable=False),
    sa.Column('semana_do_ano', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_datahora')
    )
    op.create_table('d_status_transacao',
    sa.Column('id_status_transacao', sa.Integer(), nullable=False),
    sa.Column('status_transacao', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id_status_transacao')
    )
    op.create_table('d_tipo_transacao',
    sa.Column('id_tipo_transacao', sa.Integer(), nullable=False),
    sa.Column('tipo_transacao', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id_tipo_transacao')
    )
    op.create_table('d_agencia',
    sa.Column('n_agencia', sa.Integer(), nullable=False),
    sa.Column('n_banco', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['n_banco'], ['d_banco.n_banco'], ),
    sa.PrimaryKeyConstraint('n_agencia')
    )
    op.create_table('f_transacao',
    sa.Column('id_transacao', sa.Integer(), nullable=False),
    sa.Column('n_banco_pagador', sa.Integer(), nullable=False),
    sa.Column('n_agencia_pagador', sa.Integer(), nullable=False),
    sa.Column('n_conta_pagador', sa.Integer(), nullable=False),
    sa.Column('cpfcnpj_pagador', sa.Integer(), nullable=False),
    sa.Column('chave_pix_pagador', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('n_banco_credor', sa.Integer(), nullable=False),
    sa.Column('n_agencia_credor', sa.Integer(), nullable=False),
    sa.Column('n_conta_credor', sa.Integer(), nullable=False),
    sa.Column('cpfcnpj_credor', sa.Integer(), nullable=False),
    sa.Column('chave_pix_credor', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('valor_transacao', sa.Integer(), nullable=False),
    sa.Column('data_transacao', sa.DateTime(), nullable=False),
    sa.Column('id_status_transacao', sa.Integer(), nullable=False),
    sa.Column('id_tipo_transacao', sa.Integer(), nullable=False),
    sa.Column('data_liquidada', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['cpfcnpj_credor'], ['d_clientes.cpfcnpj'], ),
    sa.ForeignKeyConstraint(['cpfcnpj_pagador'], ['d_clientes.cpfcnpj'], ),
    sa.ForeignKeyConstraint(['id_status_transacao'], ['d_status_transacao.id_status_transacao'], ),
    sa.ForeignKeyConstraint(['id_tipo_transacao'], ['d_tipo_transacao.id_tipo_transacao'], ),
    sa.ForeignKeyConstraint(['n_agencia_credor'], ['d_agencia.n_agencia'], ),
    sa.ForeignKeyConstraint(['n_agencia_pagador'], ['d_agencia.n_agencia'], ),
    sa.ForeignKeyConstraint(['n_banco_credor'], ['d_banco.n_banco'], ),
    sa.ForeignKeyConstraint(['n_banco_pagador'], ['d_banco.n_banco'], ),
    sa.PrimaryKeyConstraint('id_transacao')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('f_transacao')
    op.drop_table('d_agencia')
    op.drop_table('d_tipo_transacao')
    op.drop_table('d_status_transacao')
    op.drop_table('d_datahora')
    op.drop_table('d_clientes')
    op.drop_table('d_cep')
    op.drop_table('d_banco')
    # ### end Alembic commands ###
