from fastapi import FastAPI
from data import lista_alunos

# Itens para exemplificar async:
# async def get(db: Any = Depends(fake_db)):
# from fastapi import Depends
# from apiTools import fake_db
# from typing import Any

app = FastAPI()


@app.get("/get-alunos")
async def get():
    return lista_alunos


@app.get("/get-aluno/{id}")
async def get_by_id(id: int):
    id_int = int(id) - 1
    return lista_alunos[id_int]


@app.post("/post-aluno")
async def post(nome: str):
    new_id = len(lista_alunos) + 1
    lista_alunos.append({"id": new_id, "nome": nome})
    return lista_alunos


@app.put("/update-aluno/{id}")
async def update(id: int, nome: str):
    id_int = int(id) - 1
    aluno_update = lista_alunos[id_int]
    aluno_update["nome"] = nome
    return lista_alunos


@app.delete("/delete-aluno/{id}")
async def delete(id: int):
    id_int = int(id)
    lista_alunos.pop(id_int - 1)

    news_ids = 0
    for aluno in lista_alunos:
        news_ids += 1
        aluno["id"] = news_ids

    return lista_alunos
