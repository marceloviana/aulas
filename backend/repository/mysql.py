import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="remoto",
  database="turmaformacao"
)

class MysqlRepository:
  
  def dml(sql):
    meuCursor = mydb.cursor()
    meuCursor.execute(sql)
    mydb.commit()
    meuCursor.close()
    return True
  
  def dql(sql):
    meuCursor = mydb.cursor()
    meuCursor.execute(sql)
    meuResultado = meuCursor.fetchall()
    mydb.commit()
    meuCursor.close()
    return meuResultado
