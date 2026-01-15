from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioProduto():
    def __init__(self, db: Session):
        self.db = db

    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(
                                    nome=produto.nome,
                                    detalhes=produto.detalhes,
                                    preco=produto.preco,
                                    disponivel=produto.disponivel
        )
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto

    def listar(self):
        produtos = self.db.query(models.Produto).all()
        return produtos

    def excluir(self):
        pass

    def editar(self):
        pass

class RepositorioUsuario():
    def __init__(self, db: Session):
        self.db = db

    def criar(self, usuario: schemas.Usuario):
        db_usuario = models.Usuario(
                                    nome=usuario.nome,
                                    idade=usuario.idade,
                                    data_nascimento=usuario.data_nascimento,
                                    telefone=usuario.telefone
        )
        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)
        return db_usuario

    def listar(self):
        db_usuarios = self.db.query(models.Usuario).all()
        return db_usuarios

    def editar(self):
        pass

    def excluir(self):
        pass