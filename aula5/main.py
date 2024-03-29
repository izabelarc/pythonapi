from fastapi import FastAPI, HTTPException, status, Path
from apiTools import *
from data import lista_clientes

app = FastAPI()


@app.get("/clientes", status_code=status.HTTP_200_OK)
async def get_clientes():
    try:
        return lista_clientes
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Clientes não encontrados"
        )


@app.get("/clientes/{id}", status_code=status.HTTP_200_OK)
async def get_cliente_id(id: int):
    try:
        resposta = get_by_id(id, lista_clientes)
        return resposta
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado"
        )

@app.post("/clientes-create", status_code=status.HTTP_201_CREATED)
async def create_cliente(nombre: str, plato_favorito: str):
    try:
        resposta = create_cliente_new(nombre, plato_favorito, lista_clientes)
        return resposta
    except:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Não foi possível criar o cliente."
        )
        
@app.put("/clientes-update/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_cliente(nombre: str, plato_favorito: str, id: int):
    try:
        resposta = update_cliente_by_id(nombre, plato_favorito, id, lista_clientes)
        return resposta
    except:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Não foi possível atualizar o cliente."
        )

@app.delete("/clientes-delete/{id}", status_code=status.HTTP_202_ACCEPTED)
async def delete(id: int):
    try:
        id_int = int(id)
        lista_clientes.pop(id_int - 1)

        news_ids = 0
        for cliente in lista_clientes:
            news_ids += 1
            cliente["id"] = news_ids

        return lista_clientes
    except:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Não foi possível deletar o cliente."
        )
        
# @app.get("/clientes/{id}")
# async def get_clientes_path(id:int= Path(
#     title="ID do curso",
# )):
    