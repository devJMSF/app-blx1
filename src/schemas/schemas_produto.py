from pydantic import BaseModel
from typing import Optional
from src.schemas.schemas_usuario import Usuario

class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    tamanhos: str
    usuario_id: int
    usuario: Optional[Usuario] = None

    class Config:
        from_attribute  = True

class ProdutoSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    
    class Config:
        from_attribute  = True


