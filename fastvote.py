#resgitervote (titulo,candidato) - protocolo
#accountvote (urna) - quantidade de votos por urna/candidato
#acountvoteall () - votos gerais
import math
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Text
import sqlite3

app = FastAPI()
class Voto(BaseModel):
     titulo: Text
     candidato: int
     urna: int

@app.post("/register_vote")
def register_vote(v: Voto):
     try:
          c= sqlite3.connect('/Users/Ijovem03/projeto/eleicao/database/eleicao.db')
          cr = c.cursor()
          cr.execute("""  INSERT INTO votos  (titulo_num, candidato_num, urna_num) VALUES (?, ?, ?)        """ , ( v.titulo, v.candidato, v.urna)  )
          c.commit()
          c.close()
     except:
          return{"msg":"erro genérico"}
     else:
          return{"msg":"voto registrado com sucesso !!!"}

@app.get("/account_vote/{urna}")
def account_vote(urna: str):
     try:
          c= sqlite3.connect('/Users/Ijovem03/projeto/eleicao/database/eleicao.db')
          cr = c.cursor()
          sql = "SELECT candidato_num, count(*) FROM votos WHERE urna_num= " + urna + " GROUP BY candidato_num "

          cr.execute(sql)
          lista = cr.fetchall()    
          c.close()
          return dict(lista)
     except:
          return{"msg":"erro genérico"}

@app.get("/account_vote_all")
def account_vote_all():
     try:
          c= sqlite3.connect('/Users/Ijovem03/projeto/eleicao/database/eleicao.db')
          cr = c.cursor()
          cr.execute("""  SELECT candidato_num, count(*) FROM votos GROUP BY candidato_num"""  )
          lista = cr.fetchall()    
          c.close()
          return dict(lista)
     except:
          return{"msg":"erro genérico"}
     

@app.get("/Calcular")
def calcular(x: int):
     return {x+ math.sqrt(x)}

@app.put("/elogio")
def elogio(nome: str, sexo: str):
     if (sexo == "f") :return {"msg": "garota, tu és  deveras muito formosa ..."}
     else: return {"msg": "mano, tu é muito bonito cara..."}

@app.delete("/apagar")
def apagar():
     return {"msg": "Os dados foram apagados com sucesso!"}