from datetime import datetime, timedelta
from jose import jwt

# CRENDENCIAS
SECRET_KEY = "C6C1CA90CBAA942C5DEB8E2CDF9A5417"
ALGORITHM = "HS256"
EXPIRES_IN_MINUTES = 3000

def gerar_token_acesso(data: dict):
    dados = data.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MINUTES)

    dados.update({"exp": expiracao})

    token_jwt = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)

    return token_jwt

def verificar_token_acesso(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    return payload.get("sub")