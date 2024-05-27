from logging.config import fileConfig
from sqlmodel import SQLModel
from sqlalchemy import create_engine
import sqlmodel

from alembic import context
from src.models.transacao import *  # Importa todos os modelos

# Este é o caminho para o seu banco de dados SQLite
DATABASE_URL = "sqlite:///./db/db_transacao.db"

# Esta linha carrega a configuração de logging do arquivo .ini do alembic
fileConfig(context.config.config_file_name)

# Esta linha obtém a seção sqlalchemy da configuração do alembic
config = context.config

# Este é o objeto Engine, que usamos para acessar o banco de dados
target_metadata = SQLModel.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True, dialect_opts={"paramstyle": "named"}
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = create_engine(DATABASE_URL)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()