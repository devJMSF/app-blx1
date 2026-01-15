from pydantic import BaseModel
from typing import Optional

class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False

    class Config:
        from_attribute = True

class ProdutoSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    
    class Config:
        from_attribute = True

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    idade: int
    data_nascimento: str
    telefone: str

    class Config:
        from_attribute = True
