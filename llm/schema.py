from pydantic import BaseModel
from typing import List

class FieldEntry(BaseModel):
    code: str
    name: str
    value: float
    justification: str
    rules_used: List[str]

class CorepReport(BaseModel):
    template: str
    fields: List[FieldEntry]
    missing_data: List[str]
    validation_flags: List[str]
