import os
import psycopg 

senha = os.getenv("DB_PASSWORD")
if senha is None:
    senha = "DB_PASSWORD"
else:
    print("Erro: a senhado banco não fo configurada")

psycopg.connect(
  host="localhost",
  port=5432,
  dbname="empresa_db",
  user="admin",
  password=senha
)
