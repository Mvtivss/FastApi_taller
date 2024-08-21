from bson import ObjectId
from typing import List, Optional
from models import Benefit, BenefitResponse
from database import db

# Simulando una base de datos en memoria
benefits_collection = db["benefits"]

def benefit_to_response(benefit: dict) -> BenefitResponse:
    return BenefitResponse(
        
        name=benefit["name"],
        price=benefit["price"],
        active=benefit["active"],
        description=benefit.get("description")
    )

def create_benefit(benefit: Benefit) -> BenefitResponse:
    result = benefits_collection.insert_one(benefit.dict())
    return BenefitResponse(id=str(result.inserted_id), **benefit.dict())

def get_benefit(benefit_id: str) -> Optional[BenefitResponse]:
    benefit = benefits_collection.find_one({"_id": ObjectId(benefit_id)})
    if benefit:
        return benefit_to_response(benefit)
    return None

def get_all_benefits() -> List[BenefitResponse]:
    benefits = benefits_collection.find()
    return [benefit_to_response(benefit) for benefit in benefits]

def update_benefit(benefit_id: str, benefit: Benefit) -> Optional[BenefitResponse]:
    result = benefits_collection.update_one(
        {"_id": ObjectId(benefit_id)},
        {"$set": benefit.dict()}
    )
    if result.modified_count:
        return get_benefit(benefit_id)
    return None

def delete_benefit(benefit_id: str) -> bool:
    result = benefits_collection.delete_one({"_id": ObjectId(benefit_id)})
    return result.deleted_count > 0