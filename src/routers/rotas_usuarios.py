from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config import database
from src.infra.sqlalchemy.repositorio.repositorio_usuario import RepositorioUsuario
from src.schemas import schemas
from src.infra.providers import hash_providers

router = APIRouter()

# =================USUARIOS====================

@router.get("/usuarios",status_code=status.HTTP_200_OK, response_model=List[schemas.Usuario])
def listar_usuario(db: Session = Depends(database.get_bd)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios

@router.post("/usuario",status_code=status.HTTP_201_CREATED, response_model=schemas.UsuarioSimples)
def criar_usuario(usuario: schemas.Usuario, db: Session = Depends(database.get_bd)):
    usuario.senha = hash_providers.gerar_hash(usuario.senha)
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado

@router.put("/usuario/{id}", status_code=status.HTTP_200_OK)
def atualizar_usuario(id: int, usuario: schemas.Usuario, db: Session = Depends(database.get_bd)):
    atualizar_usuario = RepositorioUsuario(db).editar(id, usuario)
    usuario.id == id
    return atualizar_usuario

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

@router.post("/usuario/logar", response_model=schemas.UsuarioSimples)
def logar(login: schemas.UsuarioLogar, session: Session = Depends(database.get_bd)):
    email = login.email
    senha = login.senha

    usuario = RepositorioUsuario(session).buscar_usuario_por_email(email)

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario ou senha incorreto!")
    
    validar_senha = hash_providers.verificar_hash(senha, usuario.senha)

    if not validar_senha:
        raise HTTPException(status_code=404, detail="Usuario ou senha incorreto!")
    
    return usuario