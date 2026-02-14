from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session  
from src.infra.sqlalchemy.config import database
from src.infra.providers import token_providers
from src.infra.sqlalchemy.repositorio import repositorio_usuario
from jose import JWTError

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

def obter_usuario_logado(token: str = Depends(oauth2_schema), 
                         session: Session = Depends(database.get_bd)):
    
    try:
        email = token_providers.verificar_token_acesso(token)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="token inválido"
            )
    
    if not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="token inválido"
            )
    
    usuario = repositorio_usuario.RepositorioUsuario(session).buscar_usuario_por_email(email)

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="token inválido"
            )
    
    return usuario