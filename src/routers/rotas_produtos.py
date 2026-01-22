from fastapi import APIRouter
from fastapi import Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config import database
from src.infra.sqlalchemy.repositorio.repositorio_produto import RepositorioProduto
from src.schemas import schemas

router = APIRouter()

# =================PRODUTOS====================

@router.get("/produtos",status_code=status.HTTP_200_OK, response_model=List[schemas.Produto])
def listar_produtos(db: Session = Depends(database.get_bd)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@router.post("/produto", status_code=status.HTTP_201_CREATED)
def criar_produto(produto: schemas.Produto, db: Session = Depends(database.get_bd)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@router.put("/produto/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ProdutoSimples)
def atualizar_produto(id: int, produto: schemas.Produto, db: Session = Depends(database.get_bd)):
    RepositorioProduto(db).editar(id, produto)
    produto.id == id
    return produto

@router.delete("/produtos/{id}",status_code=status.HTTP_200_OK)
def deletar_produtos(id: int, db: Session = Depends(database.get_bd)):
    produtos_excluido = RepositorioProduto(db).excluir(id)
    return produtos_excluido