from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select, update, delete
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from fastapi import HTTPException, status

class RepositorioPedido():
    def __init__(self, session: Session):
        self.session = session

    def gravar(self, pedido: schemas.Pedido):
        db_pedido = models.Pedido(quantidade=pedido.quantidade,
                                local_entrega=pedido.local_entrega,
                                tipo_entrega=pedido.tipo_entrega,
                                observacao=pedido.observacao, 
                                usuario_id=pedido.usuario_id, 
                                produto_id=pedido.produto_id)
        self.session.add(db_pedido)
        self.session.commit()
        self.session.refresh(db_pedido)
        return db_pedido
    
    def buscar_por_id(self, id: int) :
        buscar_pedido = self.session.get(models.Pedido, id)

        if not buscar_pedido:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pedido não encontrado!")
        
        return buscar_pedido
    
    def listar_meus_pedidos_por_usuario_id(self, usuario_id: int):
        query = select(models.Pedido).where(models.Pedido.usuario_id == usuario_id)
        consultar_meus_pedidos = self.session.execute(query).scalars().all()
        return consultar_meus_pedidos
    
    def listar_minhas_vendas_por_usuario_id(self, usuario_id: int):
        query = select(models.Pedido).join_from(models.Pedido, models.Produto).where(models.Pedido.usuario_id == usuario_id)
        consultar_meus_pedidos = self.session.execute(query).scalars().all()
        return consultar_meus_pedidos

    
    def editar(self, id: int, pedido: schemas.Pedido):
        buscar_pedido = self.session.get(models.Pedido, id)

        if not buscar_pedido:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pedido não encontrado!")

        editar_pedido = update(models.Pedido).where(models.Pedido.id == id).values(
            quantidade=pedido.quantidade,
            local_entrega=pedido.local_entrega,
            tipo_entrega=pedido.tipo_entrega,
            observacao=pedido.observacao, 
            usuario_id=pedido.usuario_id,
            produto_id=pedido.produto_id)
        self.session.execute(editar_pedido)
        self.session.commit()
        return pedido
    
    def excluir(self, id: int):
        buscar_pedido = self.session.get(models.Pedido, id)

        if not buscar_pedido:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pedido não encontrado!")
        
        self.session.delete(buscar_pedido)
        self.session.commit()
        return "Pedido excluido com sucesso!"
    

    

        