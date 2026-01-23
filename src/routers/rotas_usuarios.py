from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config import database
from src.infra.sqlalchemy.repositorio.repositorio_usuario import RepositorioUsuario
from src.schemas import schemas

router = APIRouter()

# =================USUARIOS====================

@router.get("/usuarios",status_code=status.HTTP_200_OK, response_model=List[schemas.Usuario])
def listar_usuario(db: Session = Depends(database.get_bd)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios

@router.post("/usuario",status_code=status.HTTP_201_CREATED, response_model=schemas.UsuarioSimples)
def criar_usuario(usuario: schemas.Usuario, db: Session = Depends(database.get_bd)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado

@router.put("/usuario/{id}", status_code=status.HTTP_200_OK, response_model=schemas.UsuarioSimples)
def atualizar_usuario(id: int, usuario: schemas.Usuario, db: Session = Depends(database.get_bd)):
    RepositorioUsuario(db).editar(id, usuario)
    usuario.id == id
    return usuario

@router.delete("/usuario/{id}",status_code=status.HTTP_200_OK)
def deletar_produtos(id: int, db: Session = Depends(database.get_bd)):
    usuario_excluido = RepositorioUsuario(db).excluir(id)
    return usuario_excluido

@router.get("/usuario/{id}")
def consultar_usuario(id: int, db: Session = Depends(database.get_bd)):
    localizar_usuario = RepositorioUsuario(db).buscar_usuario(id)
    if not localizar_usuario:
        raise HTTPException(status_code=404, detail=f"não existe usuario com o id [{id}]!")
    return localizar_usuario
