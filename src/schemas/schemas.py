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

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    idade: int
    data_nascimento: str
    telefone: str
    # produtos: List[produtos] = []

    class Config:
        from_attribute = True
