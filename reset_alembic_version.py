from sqlalchemy import create_engine, text
from os import getenv

DATABASE_URL = getenv("DATABASE_URL", "sqlite:///./fluxo.db")
engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    conn.execute(text("DELETE FROM alembic_version;"))  # Use sqlalchemy.text para comandos SQL
    conn.commit()
    print("Tabela alembic_version foi resetada.")