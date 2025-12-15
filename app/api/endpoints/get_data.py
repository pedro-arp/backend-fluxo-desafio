from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.db.schemas import PaginationResponse, LightingPostResponse
from app.db.crud import get_lighting_posts
from typing import Optional

get_router = APIRouter(prefix="/lighting-posts", tags=["lighting-posts"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@get_router.get("/", response_model=PaginationResponse)
def get_lighting_posts_endpoint(
    db: Session = Depends(get_db),
    lamp_type: Optional[str] = Query(None, description="Filtrar por tipo de lâmpada"),
    needs_repair: Optional[bool] = Query(None, description="Filtrar por manutenção"),
    page: int = Query(1),
    page_size: int = Query(10),
):
    skip = (page - 1) * page_size
    posts = get_lighting_posts(db, lamp_type, needs_repair, skip, page_size)

    formatted_posts = [
        {
            "id": post.id,
            "address": post.address,
            "location": {"lat": post.latitude, "long": post.longitude},
            "equipment": {
                "type": post.lamp_type,
                "wattage": post.wattage,
                "voltage": post.voltage,
            },
            "maintenance": {
                "needs_repair": post.needs_repair,
                "last_maintenance": post.last_maintenance.isoformat(),
            },
        }
        for post in posts
    ]

    return {
        "page": page,
        "page_size": page_size,
        "total": len(formatted_posts),
        "posts": formatted_posts,
    }
