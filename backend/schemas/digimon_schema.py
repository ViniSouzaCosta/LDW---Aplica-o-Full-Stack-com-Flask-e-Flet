from pydantic import BaseModel

class DigimonSchema(BaseModel):
    nome: str
    nivel: str