from pydantic import BaseModel
from typing import Optional, List

class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    tamanho: str = False

    class Config:
        from_attribute = True

class ProdutoSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    
    class Config:
        from_attribute = True


