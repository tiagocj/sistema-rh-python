from fastapi import FastAPI #fastAPI:biblioteca de criação de APIs e backends web
import sqlite3

app = FastAPI() # cria um objeto FastAPI e app aponta para esse objeto


@app.get("/") # "/" é a raiz do sistema (@decorator)
#@app.get("/") → "FastAPI, registre a função abaixo para atender requisições GET no endereço /."
def inicio(): #É o q o python executará quando alguém fizer um get
    return {"mensagem": "Sistema de RH funcionando"}

@app.get("/funcionarios")
def listar_funcionarios():
    conexao = sqlite3.connect("rh.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()

    conexao.close()

    lista_funcionarios = []

    for funcionario in funcionarios:
        lista_funcionarios.append({
            "id": funcionario[0],
            "nome": funcionario[1],
            "cargo": funcionario[2],
            "salario": funcionario[3]
        })

    return lista_funcionarios

@app.get("/funcionarios/{id}")
def buscar_funcionario(id: int):
    conexao = sqlite3.connect("rh.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM funcionarios WHERE id = ?", (id))

    funcionario = cursor.fetchone()

    conexao.close()

    return funcionario