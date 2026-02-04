from sqlalchemy.orm import Session, joinedload
from sqlalchemy import update, delete, select
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from fastapi import HTTPException, status

class RepositorioProduto():
    def __init__(self, session: Session):
        self.session = session

    def criar(self, produto: schemas.Produto):
        buscar_produto = select(models.Produto).where(
            models.Produto.nome == produto.nome,
            models.Produto.detalhes == produto.detalhes,
            models.Produto.disponivel == produto.disponivel,
            models.Produto.preco == produto.preco,
            models.Produto.tamanhos == produto.tamanhos)
        
        query = self.session.execute(buscar_produto).scalar_one_or_none()

        if query:
            raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Produto já existe!")

        db_produto = models.Produto(
                                    nome=produto.nome,
                                    detalhes=produto.detalhes,
                                    preco=produto.preco,
                                    disponivel=produto.disponivel,
                                    tamanhos=produto.tamanhos,
                                    usuario_id=produto.usuario_id,
        )
        self.session.add(db_produto)
        self.session.commit()
        self.session.refresh(db_produto)
        return db_produto

    def listar(self):
        produtos = self.session.query(models.Produto).options(joinedload(models.Produto.usuario)).all()
        return produtos
 
    def editar(self, id: int, produto: schemas.Produto):
        buscar_procuto = self.session.get(models.Produto, id)

        if not buscar_procuto:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado!")

        editar_produto = update(models.Produto).where(models.Produto.id == id).values(
                                nome=produto.nome,
                                detalhes=produto.detalhes,
                                preco=produto.preco,
                                disponivel=produto.disponivel,
                                tamanhos=produto.tamanhos)
        self.session.execute(editar_produto)
        self.session.commit()
        return produto    
    
    def excluir(self, id: int):
        buscar_produto = self.session.get(models.Produto, id)

        if not buscar_produto:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado!")

        query = delete(models.Produto).where(models.Produto.id == id)
        self.session.execute(query)
        self.session.commit()
        return {"mensagem": "produto deletado!"}

    def buscar_item(self, id: int):
        buscar_produto = self.session.get(models.Produto, id)

        if not buscar_produto:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado!")
        
        query = select(models.Produto).where(models.Produto.id == id)
        consulta_produto = self.session.execute(query).first()
        return consulta_produto

