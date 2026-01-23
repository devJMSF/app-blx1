from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioUsuario():
    def __init__(self, db: Session):
        self.session = db

    def criar(self, usuario: schemas.Usuario):
        db_usuario = models.Usuario(
                                    nome=usuario.nome,
                                    idade=usuario.idade,
                                    data_nascimento=usuario.data_nascimento,
                                    telefone=usuario.telefone,
                                    email=usuario.email,
                                    senha=usuario.senha
                                    )
        self.session.add(db_usuario)
        self.session.commit()
        self.session.refresh(db_usuario)
        return db_usuario

    def listar(self): 
        smtm = select(models.Usuario) 
        usuarios = self.session.execute(smtm).scalars().all() 
        return usuarios

    def editar(self, id: int, usuario: schemas.Usuario):
        editar_usuario = update(models.Usuario).where(models.Usuario.id == id).values(
                                    nome=usuario.nome,
                                    idade=usuario.idade,
                                    data_nascimento=usuario.data_nascimento,
                                    telefone=usuario.telefone,
                                    email=usuario.email,
                                    senha=usuario.senha)
        self.session.execute(editar_usuario)
        self.session.commit()
        return usuario

    def excluir(self, id: int):
        excluir_usuario = delete(models.Usuario).where(models.Usuario.id == id)
        self.session.execute(excluir_usuario)
        self.session.commit()
        return id
    
    def buscar_usuario(self, id: int):
        localizar_usuario = select(models.Usuario).where(models.Usuario.id == id)
        consulta_produto = self.session.execute(localizar_usuario).first()
        return consulta_produto
