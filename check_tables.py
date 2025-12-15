from sqlalchemy import create_engine, inspect
from os import getenv

DATABASE_URL = getenv("DATABASE_URL", "sqlite:///./fluxo.db")

engine = create_engine(DATABASE_URL)

inspector = inspect(engine)

print("Tabelas no banco de dados:")
print(inspector.get_table_names())