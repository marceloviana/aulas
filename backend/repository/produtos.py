import mysql.connector, json
import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="remoto",
  database="turmaformacao"
)

class ProdutoRepository:
    
    def criar(self, sql):
        meuCursor = mydb.cursor()
        meuCursor.execute(sql)
        meuCursor.close()
        mydb.commit()
        return True
    
    def atualizar():
       return True
    
    def ler(self, sql):
        meuCursor = mydb.cursor()
        meuCursor.execute(sql)
        meuResultado = meuCursor.fetchall()
        meuCursor.close()
        mydb.commit()
        return meuResultado
    
