from sqlalchemy import Column, Integer, String, Boolean, Float, Date
from app.db import Base

class LightingPost(Base):
    __tablename__ = "lighting_posts"

    id = Column(String, primary_key=True, unique=True)
    address = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    lamp_type = Column(String, nullable=False)
    wattage = Column(Integer, nullable=False)
    voltage = Column(Integer, nullable=False)
    needs_repair = Column(Boolean, nullable=False)
    last_maintenance = Column(Date, nullable=True)
    installation_date = Column(Date, nullable=True)
    hours_in_operation = Column(Integer, nullable=False)

