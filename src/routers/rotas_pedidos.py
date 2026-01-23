from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config import database
from src.infra.sqlalchemy.repositorio import repositorio_pedido
from src.schemas import schemas

router = APIRouter()

@router.post("/pedido", status_code=status.HTTP_201_CREATED)
def criar_pedido(pedido: schemas.Pedido, db: Session = Depends(database.get_bd)):
    pass

@router.get("/pedidos")
def listar_produtos(db: Session = Depends(database.get_bd)):
    pass

@router.get("/pedido/{id}")
def consultar_produto(id: int, db: Session = Depends(database.get_bd)):
    pass

@router.put("/pedido/{id}")
def atualizar_produto(id: int, db: Session = Depends(database.get_bd)):
    pass

@router.delete("/pedido/{id}")
def cancelar_produto(id: int, db: Session = Depends(database.get_bd)):
    pass