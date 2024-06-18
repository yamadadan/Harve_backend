from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import APIKeyHeader

# Criação do aplicativo FastAPI
app = FastAPI()

# Definição da chave de API (normalmente você obteria isso de um banco de dados ou variável de ambiente)
API_KEY = "mysecretapikey"
API_KEY_NAME = "access_token"

# Instância de APIKeyHeader para obter a chave de API do cabeçalho
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

# Função para verificar a chave de API
async def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API Key",
        )
    return api_key

# Endpoint protegido por chave de API
@app.get("/protected-route")
async def protected_route(api_key: str = Depends(get_api_key)):
    return {"message": "You have access to this protected route!"}

# Endpoint público
@app.get("/public-route")
async def public_route():
    return {"message": "This is a public route. No API key required."}

