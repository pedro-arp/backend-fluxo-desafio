from sqlalchemy.orm import Session
from app.db.models import LightingPost
from typing import Iterable, Set

def get_lighting_posts(db: Session, lamp_type: str, needs_repair: bool, skip: int, limit: int):
    query = db.query(LightingPost)

    if lamp_type:
        query = query.filter(LightingPost.lamp_type == lamp_type)
    if needs_repair is not None:
        query = query.filter(LightingPost.needs_repair == needs_repair)

    return query.offset(skip).limit(limit).all()


def bulk_insert_lighting_posts(db: Session, posts_data: list[dict]):
    objects = [LightingPost(**data) for data in posts_data]
    db.bulk_save_objects(objects)
    db.commit()
    return len(objects)


def get_existing_lighting_post_ids(db: Session, ids: Iterable) -> Set:

    ids_list = [i for i in ids if i is not None]
    if not ids_list:
        return set()
    q = db.query(LightingPost.id).filter(LightingPost.id.in_(ids_list)).all()
    return set(r[0] for r in q)

