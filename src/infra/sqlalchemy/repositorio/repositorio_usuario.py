from sqlalchemy.orm import Session
from sqlalchemy import select
from src.schemas import schemas_usuario
from src.infra.sqlalchemy.models import models

class RepositorioUsuario():
    def __init__(self, db: Session):
        self.db = db

    def criar(self, usuario: schemas_usuario.Usuario):
        db_usuario = models.Usuario(
                                    nome=usuario.nome,
                                    idade=usuario.idade,
                                    data_nascimento=usuario.data_nascimento,
                                    telefone=usuario.telefone,
                                    email=usuario.email,
                                    senha=usuario.senha
                                    )
        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)
        return db_usuario

    def listar(self): 
        smtm = select(models.Usuario) 
        usuarios = self.db.execute(smtm).scalars().all() 
        return usuarios

    def editar(self):
        pass

    def excluir(self):
        pass