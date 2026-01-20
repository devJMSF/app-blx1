from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config import database
from src.infra.sqlalchemy.repositorio.produto import RepositorioProduto, RepositorioUsuario
from src.schemas import schemas

database.criar_bd()

app = FastAPI()

# =================PRODUTOS====================

@app.get("/produtos",status_code=status.HTTP_200_OK)
def listar_produtos(db: Session = Depends(database.get_bd)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@app.post("/produto", status_code=status.HTTP_201_CREATED)
def criar_produto(produto: schemas.Produto, db: Session = Depends(database.get_bd)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return  produto_criado

# =================USUARIOS====================

@app.get("/usuarios",status_code=status.HTTP_200_OK)
def listar_usuario(db: Session = Depends(database.get_bd)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios

@app.post("/usuario",status_code=status.HTTP_201_CREATED)
def criar_usuario(usuario: schemas.Usuario, db: Session = Depends(database.get_bd)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado
