from pydantic import BaseModel
from typing import List

# Modelo para representar localizações
class Location(BaseModel):
    lat: float
    long: float

# Modelo para representar detalhes de equipamentos
class Equipment(BaseModel):
    type: str
    wattage: int
    voltage: int

# Modelo para representar detalhes de manutenção
class Maintenance(BaseModel):
    needs_repair: bool
    last_maintenance: str

# Modelo para postes de iluminação
class LightingPostResponse(BaseModel):
    id: str
    address: str
    location: Location
    equipment: Equipment
    maintenance: Maintenance

    class Config:
        orm_mode = True

# Modelo para respostas com paginação
class PaginationResponse(BaseModel):
    page: int
    page_size: int
    total: int
    posts: List[LightingPostResponse]