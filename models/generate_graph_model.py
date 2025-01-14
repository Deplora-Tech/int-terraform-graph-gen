from pydantic import BaseModel
from typing import Dict

class GenerateGraphModel(BaseModel):
    id: str
    files: Dict[str, str]

