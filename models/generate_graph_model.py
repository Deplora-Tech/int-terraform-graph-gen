from pydantic import BaseModel
from typing import Dict

class GenerateGraphModel(BaseModel):
    id: str
    file: Dict[str, str]

