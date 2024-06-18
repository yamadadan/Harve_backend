import mysql.connector
from fastapi import FastAPI, HTTPException

# Configuração de conexão com o banco de dados MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="db_name"
)

# Rota para inserir categorias de produtos no banco de dados
@app.post("/inserir-categorias/")
async def inserir_categorias(categorias: list):
    cursor = conn.cursor()
    try:
        # Iterar sobre as categorias recebidas e inserir no banco de dados
        for categoria in categorias:
            nome = categoria.get("nome")
            id = categoria.get("id")
            if nome is None or id is None:
                raise HTTPException(status_code=400, detail="Os campos 'nome' e 'id' são obrigatórios.")
            cursor.execute("INSERT INTO categorias (id, nome) VALUES (%s, %s)", (id, nome))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao inserir categorias: {e}")
    finally:
        cursor.close()
