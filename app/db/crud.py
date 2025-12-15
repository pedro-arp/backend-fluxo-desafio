from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.db.models import LightingPost

# Função para buscar um registro pelo ID do poste
def get_lighting_post_by_id(db: Session, post_id: int):
    return db.query(LightingPost).filter(LightingPost.id == post_id).first()

# Função para listar registros com filtros e paginação
def get_lighting_posts(db: Session, lamp_type: str, needs_repair: bool, skip: int, limit: int):
    query = db.query(LightingPost)

    if lamp_type:
        query = query.filter(LightingPost.lamp_type == lamp_type)
    if needs_repair is not None:
        query = query.filter(LightingPost.needs_repair == needs_repair)

    return query.offset(skip).limit(limit).all()

# Função para inserir um registro no banco verificando duplicatas
def insert_lighting_post(db: Session, post_data: dict):
    exists = db.query(LightingPost).filter(LightingPost.id == post_data["id"]).first()
    if exists:
        return None  # Registro duplicado
    post = LightingPost(**post_data)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def bulk_insert_lighting_posts(db: Session, posts_data: list[dict]):
    objects = [LightingPost(**data) for data in posts_data]  # Converte os dicionários em objetos ORM
    db.bulk_save_objects(objects)  # Realiza o bulk insert
    db.commit()
    return len(objects)  # Retorna o número de objetos inseridos