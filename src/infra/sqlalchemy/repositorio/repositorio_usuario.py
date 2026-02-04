from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from fastapi import HTTPException, status

class RepositorioUsuario():
    def __init__(self, db: Session):
        self.session = db

    def criar(self, usuario: schemas.Usuario):
        query = select(models.Usuario).where(models.Usuario.email == usuario.email)
        buscar_usuario = self.session.scalar(query)

        if buscar_usuario:
            raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Usuário já existe!")
        
        db_usuario = models.Usuario(
                                    nome=usuario.nome.lower(),
                                    idade=usuario.idade,
                                    data_nascimento=usuario.data_nascimento,
                                    telefone=usuario.telefone,
                                    email=usuario.email.lower(),
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
        buscar_usuario = self.session.get(models.Usuario, id)

        if not buscar_usuario:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario não encontrado!")


        editar_usuario = update(models.Usuario).where(models.Usuario.id == id).values(
                                    nome=usuario.nome,
                                    idade=usuario.idade,
                                    data_nascimento=usuario.data_nascimento,
                                    telefone=usuario.telefone,
                                    email=usuario.email,
                                    senha=usuario.senha)
        self.session.execute(editar_usuario)
        self.session.commit()
        return "Usuario atualizado com sucesso!"

    def excluir(self, id: int):
        buscar_usuario = self.session.get(models.Usuario, id)

        if not buscar_usuario:
            raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Usuario não encontrado!")
        
        self.session.delete(buscar_usuario)
        self.session.commit()
        return "Usuario excluido com sucesso!"
    
    def buscar_usuario(self, id: int):
        localizar_usuario = select(models.Usuario).where(models.Usuario.id == id)
        consulta_produto = self.session.execute(localizar_usuario).first()
        return consulta_produto
    
    def buscar_usuario_por_email(self, email: str) -> schemas.Usuario:
        localizar_usuario = select(models.Usuario).where(models.Usuario.email == email)        
        return self.session.execute(localizar_usuario).scalar()
