from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from src.infra.sqlalchemy.config.database import Base

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    data_nascimento = Column(String)
    telefone = Column(String)
    email = Column(String)
    senha = Column(String) 

    produtos = relationship("Produto", back_populates="usuario")

class Produto(Base):
    __tablename__ = "produto"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    detalhes = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)
    tamanhos = Column(String)
    usuario_id = Column(Integer, ForeignKey("usuario.id", name="fk_usuario"))
    
    usuario = relationship("Usuario", back_populates="produtos")