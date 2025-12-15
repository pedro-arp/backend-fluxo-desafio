from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.db.models import LightingPost

# Inicializa a conexão com o banco
db: Session = SessionLocal()

# Consulta todos os registros
posts = db.query(LightingPost).all()

print("Registros na tabela lighting_posts:")
for post in posts:
    print(f"ID: {post.id}, Endereço: {post.address}, Tipo de Lâmpada: {post.lamp_type}, Precisa de Manutenção: {post.needs_repair}")

# Fecha a conexão com o banco
db.close()