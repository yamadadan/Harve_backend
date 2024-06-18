from fastapi import FastAPI, Header, Query
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Configuração do CORS
origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

categorias_produtos = [
    {"id":1, "nome": 'Eletrônicos'},
    {"id":2, "nome": 'Roupas'},
    {"id":3, "nome": 'Livros'},
]

# Rota para listar categorias de produtos
@app.get("/categorias-produtos", response_model=List[dict])
async def listar_categorias():
    return categorias_produtos

# Rota para obter uma categoria de produto específica pelo ID
@app.get("/categorias-produtos/{categoria_id}", response_model=dict)
async def obter_categoria(categoria_id: int):
    for categoria in categorias_produtos:
        if categoria['id'] == categoria_id:
            return categoria
    return {'erro': 'Categoria não encontrada'}

# Rota para obter uma categoria de produto específica pelo ID passado no header
@app.get("/categorias-produtos-header-id", response_model=dict)
async def obter_categoria_header(id: str = Header(...)):
    for categoria in categorias_produtos:
        if categoria['id'] == int(id):
            return categoria
    return {'erro': 'Categoria não encontrada'}

# Rota para obter uma categoria de produto específica pelo ID passado no header
@app.get("/categorias-produtos-query/", response_model=dict)
async def obter_categoria_header(id: int = Query(...)):
    for categoria in categorias_produtos:
        if categoria['id'] == id:
            return categoria
    return {'erro': 'Categoria não encontrada'}

# Rota para obter uma categoria de produto específica pelo ID ou nome passado no header
@app.get("/categorias-produtos-header-2/id2", response_model=dict)
async def obter_categoria_header_2param(id2: int = Header(None), nome: str = Header(None)):
    if id2 is not None:
        for categoria in categorias_produtos:
            if categoria['id'] == id2:
                return categoria
        return {'erro': 'Categoria não encontrada com o ID fornecido'}
    elif nome is not None:
        for categoria in categorias_produtos:
            if categoria['nome'].lower() == nome.lower():
                return categoria
        return {'erro': 'Categoria não encontrada com o nome fornecido'}
    else:
        return {'erro': 'Por favor, forneça o ID ou o nome da categoria no cabeçalho'}

# Rota para inserir categorias de produtos no banco de dados
@app.post("/inserir-categorias/", response_model=List)
async def inserir_categorias(categorias: List[str]):
    print(type(categorias))
    categorias_inseridas = []
    for categoria in categorias:
        # inserir_categoria(categoria.nome, categoria.id)
        categorias_inseridas.append(categoria)
    return categorias_inseridas
    
# Modelo para dados no body
class Produto(BaseModel):
    nome: str
    preco: float

# Rota com query parameters
@app.get("/produtos")
async def listar_produtos(categoria: str = Query(None)):
    # Lógica para listar produtos com filtro por categoria, se fornecida
    return {"categoria": categoria}

# Rota com header parameter
@app.get("/preco-produto")
async def obter_preco_produto(
    produto_id: int,
    user_agent: str = Header(None)
):
    # Lógica para obter o preço de um produto com base no user agent, se fornecido
    return {"produto_id": produto_id, "user_agent": user_agent}

# Rota com body parameter
@app.post("/criar-produto")
async def criar_produto(produto: Produto):
    # Lógica para criar um novo produto com os dados fornecidos no corpo da requisição
    return {"nome": produto.nome, "preco": produto.preco}