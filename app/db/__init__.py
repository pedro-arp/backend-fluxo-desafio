from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from os import getenv

DATABASE_URL = getenv("DATABASE_URL", "sqlite:///./fluxo.db")

# Nos sistemas baseados em SQLite podemos desabilitar `check_same_thread` para evitar problemas com threads.
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()