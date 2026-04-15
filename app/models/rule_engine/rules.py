from pydantic import BaseModel

class RuleData(BaseModel):
    id: int
    name: str
    description: str
    is_active: bool

class RuleCreate(BaseModel):
    rule_id: int
    name: str
    description: str
    is_active: bool
    Income: int
    operator: str
    value: int
