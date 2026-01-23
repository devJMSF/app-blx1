from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config import database
from src.utils import urls
from src.routers import rotas_usuarios, rotas_produtos, rotas_pedidos

# criar o banco
database.criar_bd()

app = FastAPI()

# cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=urls.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# rotas produtos
app.include_router(rotas_produtos.router)

# rotas usuarios
app.include_router(rotas_usuarios.router)

# rotas pedidos
app.include_router(rotas_pedidos.router)

