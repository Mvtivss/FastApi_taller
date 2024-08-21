from fastapi import APIRouter, HTTPException
from typing import List
from models import Benefit, BenefitResponse
import crud

router = APIRouter()

@router.post("/benefits/", response_model=BenefitResponse)
def create_benefit(benefit: Benefit):
    return crud.create_benefit(benefit)

@router.get("/benefits/{benefit_id}", response_model=BenefitResponse)
def read_benefit(benefit_id: int):
    benefit = crud.get_benefit(benefit_id)
    if benefit is None:
        raise HTTPException(status_code=404, detail="Benefit not found")
    return benefit

@router.get("/benefits/", response_model=List[BenefitResponse])
def read_all_benefits():
    return crud.get_all_benefits()

@router.put("/benefits/{benefit_id}", response_model=BenefitResponse)
def update_benefit(benefit_id: int, benefit: Benefit):
    updated_benefit = crud.update_benefit(benefit_id, benefit)
    if updated_benefit is None:
        raise HTTPException(status_code=404, detail="Benefit not found")
    return updated_benefit

@router.delete("/benefits/{benefit_id}", response_model=bool)
def delete_benefit(benefit_id: int):
    success = crud.delete_benefit(benefit_id)
    if not success:
        raise HTTPException(status_code=404, detail="Benefit not found")
    return success