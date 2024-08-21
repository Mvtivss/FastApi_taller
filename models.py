from pydantic import BaseModel
from typing import Optional

#Modelo pydantic para el beneficio
class Benefit(BaseModel):
    name: str 
    price: float
    active: bool
    description: Optional[str] = None

# Modelo pydantic para la respuesta del beneficio
class BenefitResponse(BaseModel):
    name: str 
    price: float
    active: bool
    description: Optional[str] = None