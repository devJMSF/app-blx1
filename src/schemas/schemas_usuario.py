from pydantic import BaseModel
from typing import Optional, List

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    idade: int
    data_nascimento: str
    telefone: str
    email: str
    senha: str
    # produtos: List[produtos] = []

    class Config:
        from_attribute = True