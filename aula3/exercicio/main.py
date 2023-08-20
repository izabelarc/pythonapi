"""
get todos clientes sem os dados/keys: peso, altura e as avaliações (For e HOF)
get cliente todas avaliações
get cliente última avaliação
post: com primeira avaliação (nome, peso, altura, data)
update: mudando peso, coloca nova avaliação no []
delete: simples
"""


from fastapi import FastAPI, Depends, HTTPException, status
from data import lista_clientes
from apiTols import fake_db
from typing import Any

app = FastAPI()


@app.get("/get_alunos", status_code=status.HTTP_200_OK)
async def get(db: Any = Depends(fake_db)):
    try:
        return
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Aluno não encontrado"
        )


@app.delete("/delete-alunos/{id}")
async def delete(id: int):
    id_int = int(id)
    lista_clientes.pop(id_int - 1)
    news_ids = 0

    for aluno in lista_clientes:
        news_ids += 1
        aluno["id"] = news_ids

    return lista_clientes


@app.get("/get_avaliacoes", status_code=status.HTTP_200_OK)
async def get(id: int):
    try:
        id_int = int(id) - 1
        return lista_clientes(id_int)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Aluno não encontrado"
        )


@app.get("/get_ultima", status_code=status.HTTP_200_OK)
async def get(id: int):
    try:
        id_int = int(id)
        avaliacao = []
        for cliente in lista_clientes:
            if cliente["id"] == id_int:
                avaliacao.append(
                    {"id": cliente["id"], "avaliações": cliente["avaliações"]}
                )
                return avaliacao
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Aluno não encontrado"
        )
