from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config import database
from src.infra.sqlalchemy.repositorio.repositorio_pedido import RepositorioPedido
from src.schemas import schemas

router = APIRouter()

@router.post("/pedido", status_code=status.HTTP_201_CREATED, response_model=schemas.Pedido)
def fazer_pedido(pedido: schemas.Pedido, db: Session = Depends(database.get_bd)):
    pedido_solicitado =  RepositorioPedido(db).gravar(pedido)
    return pedido_solicitado

@router.get("/pedido/{id}")
def exibir_pedido(id: int, db: Session = Depends(database.get_bd)):
    try:
        pedido = RepositorioPedido(db).buscar_por_id(id)
        return pedido
    except:
        raise HTTPException(status_code=404, detail=f"não existe pedido com o id [{id}]")

@router.get("/pedidos/{usuario_id}/compras", response_model=List[schemas.Pedido])
def listar_pedidos(usuario_id: int, db: Session = Depends(database.get_bd)):
    try:
        pedido_id = RepositorioPedido(db).listar_meus_pedidos_por_usuario_id(usuario_id)
        return pedido_id
    except:
        raise HTTPException(status_code=404, detail=f"não existe pedido com o id [{id}]")

@router.get("/pedidos/{usuario_id}/vendas", response_model=List[schemas.Pedido])
def listar_vendas(usuario_id: int, db: Session = Depends(database.get_bd)):
    pedido_id = RepositorioPedido(db).listar_minhas_vendas_por_usuario_id(usuario_id)
    if not pedido_id:
        raise HTTPException(status_code=404, detail=f"não tem pedido com o id [{usuario_id}]")
    return pedido_id


@router.put("/pedido/{id}", response_model=schemas.Pedido)
def atualizar_pedido(id: int, pedido: schemas.Pedido, db: Session = Depends(database.get_bd)):
    RepositorioPedido(db).editar(id, pedido)
    pedido.id = id
    return pedido

@router.delete("/pedido/{id}")
def cancelar_pedido(id: int, db: Session = Depends(database.get_bd)):
    pedido_excluido = RepositorioPedido(db).excluir(id)
    return pedido_excluido