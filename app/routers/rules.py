from fastapi import APIRouter, HTTPException
import app.models.rule_engine.rules as rules

router = APIRouter()


@router.post("/rules")
def create_rule(rule: rules.RuleCreate):
    return {
        "rule_id": rule.rule_id,
        "rule_name": rule.name,
        "rule_description": rule.description,
        "is_active": rule.is_active,
        "Income": rule.Income,
        "operator": rule.operator,
        "value": rule.value,
    }


@router.get("/rules/{rule_id}")
def read_rule(rule_id: int):
    # Placeholder for fetching a rule by ID
    return {
            "rule_id": rule_id, 
            "name": "Sample Rule", 
            "description": "This is a sample rule.", "is_active": True}  
