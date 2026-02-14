from pydantic import BaseModel
from typing import Optional, List

class ProdutoSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    preco: float
    
    class Config:
        from_attributes  = True

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    idade: int
    data_nascimento: str
    telefone: str
    email: str
    senha: str
    produtos: List[ProdutoSimples] = []

    class Config:
        from_attributes = True


class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    email: str

    class Config:
        from_attributes = True

class UsuarioLogar(BaseModel):
    email: str
    senha: str  

class UsuarioLogado(BaseModel):
    usuario: UsuarioSimples
    access_token: str

class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    tamanhos: str
    usuario_id: Optional[int] = None
    usuario: Optional[UsuarioSimples] = None

    class Config:
        from_attributes  = True

class Pedido(BaseModel):
    id: Optional[int] = None
    quantidade: int
    local_entrega: Optional[str]
    tipo_entrega: str
    observacao: Optional[str] = "sem observacoes"

    usuario_id: Optional[int] = None
    produto_id: Optional[int] = None

    usuario: Optional[UsuarioSimples] = None
    produto: Optional[ProdutoSimples] = None

    class Config:
        from_attributes  = True

class PedidoSimples(BaseModel):
    id: Optional[int] = None
    quantidade: int
    local_entrega: Optional[str]
    tipo_entrega: str
    observacao: Optional[str] = "sem observacoes"

    usuario_id: Optional[int] = None
    produto_id: Optional[int] = None

    









