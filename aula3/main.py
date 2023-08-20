from fastapi import FastAPI, Depends, HTTPException, status
from data import cursos
from apiTols import fake_db
from typing import Any

app = FastAPI()


@app.get("/cursos", status_code=status.HTTP_200_OK)
async def get(db: Any = Depends(fake_db)):
    # return cursos
    try:
        return cursos
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Cursos não encontrados"
        )


@app.get("/curso-get/{id}", status_code=status.HTTP_200_OK)
async def get_by_id(id: int):
    id_int = int(id) - 1
    return cursos[id_int]


@app.post("/curso-post", status_code=status.HTTP_202_CREATED)
async def post(nome: str):
    new_id = len(cursos) + 1
    cursos.append({"id": new_id, "nome": nome})
    return cursos


@app.put("/curso-update/{id}", status_code=status.HTTP_202_ACEPTED)
async def update(id: int, nome: str):
    id_int = int(id) - 1
    aluno_update = cursos[id_int]
    aluno_update["nome"] = nome
    return cursos


@app.delete("/cursos-delete/{id}")
async def delete(id: int):
    id_int = int(id)
    cursos.pop(id_int - 1)

    news_ids = 0
    for aluno in cursos:
        news_ids += 1
        aluno["id"] = news_ids

    return cursos
