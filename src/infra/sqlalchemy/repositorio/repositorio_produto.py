from sqlalchemy.orm import Session, joinedload
from src.schemas import schemas_produto
from src.infra.sqlalchemy.models import models

class RepositorioProduto():
    def __init__(self, db: Session):
        self.db = db

    def criar(self, produto: schemas_produto.Produto):
        db_produto = models.Produto(
                                    nome=produto.nome,
                                    detalhes=produto.detalhes,
                                    preco=produto.preco,
                                    disponivel=produto.disponivel,
                                    tamanhos=produto.tamanhos,
                                    usuario_id=produto.usuario_id,
        )
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto

    def listar(self):
        produtos = self.db.query(models.Produto).options(joinedload(models.Produto.usuario)).all()
        return produtos

    def excluir(self):
        pass

    def editar(self):
        pass

