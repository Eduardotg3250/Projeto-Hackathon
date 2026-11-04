import sqlite3
from fastapi import FastAPI
from fastapi import Form
import uvicorn
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(mode="debug")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

banco = sqlite3.connect("disciplinas.db")
cursor = banco.cursor()

@app.post("/disciplinas/")
def create_table(codigo: Annotated[str, Form()],
                nome: Annotated[str, Form()],
                nota: Annotated[float, Form()],
                frequencia: Annotated[float, Form()],
                professor: Annotated[str, Form()], 
                dias_da_semana: Annotated[str, Form()]
                ):
   
   cursor.execute("CREATE TABLE disciplinas(codigo text primary key NOT NULL, nome text, notas float, frequencia float, professor text, dias_da_semana text)")

@app.get("/disciplinas/")
def read_table() :
    banco = sqlite3.connect("disciplinas.db")
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM disciplinas")
    x = list(cursor.fetchall())
    cursor.close()
    banco.close()
    return x
    #for contribuinte in cursor.fetchall():
    #   print(contribuinte)

def alter_table(codigo, nome, nota, frequencia, professor, dias_da_semana):
    cursor.execute("INSERT INTO disciplinas VALUES(:codigo, :nome, :notas, :frequencia, :professor, :dias_da_semana)", 
                   {'codigo': codigo,
                    'nome': nome,
                    'notas': nota,
                    'frequencia': frequencia,
                    'professor': professor,
                    'dias_da_semana': dias_da_semana})
    banco.commit()

uvicorn.run(app)