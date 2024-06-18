import pandas as pd
from sqlalchemy import text, create_engine

# Configurações de conexão
credenciais = {
  "usuario": 'alunosqlharve',
  "senha": 'Ed&ktw35j',
  "host": 'ip-45-79-142-173.cloudezapp.io',
  "port": 3306,
  "banco_de_dados": 'modulosql'
}

STRING_CONEXAO = f"mysql+pymysql://{credenciais['usuario']}:{credenciais['senha']}@{credenciais['host']}:{credenciais['port']}/{credenciais['banco_de_dados']}"
# Cria a engine
engine = create_engine(STRING_CONEXAO)
# conn_obj = engine.connect()

# query = "SELECT * FROM cliente"
# df = pd.read_sql(text(query), conn_obj)
# conn_obj.close()
# print(df)
data = {
    'nome': 'teste',
    'cpf': '21334456',
    'idade': 32
}
df = pd.DataFrame([data])

# Nome da tabela no banco de dados
nome_da_tabela = 'cliente'

# Inserir dados
with engine.connect() as conexao:
    df.to_sql(name = nome_da_tabela, con=conexao, if_exists='append', index=False)
    
# Inserir dados usando to_sql
# df.to_sql(nome_da_tabela, con=engine, if_exists='append', index=False)
