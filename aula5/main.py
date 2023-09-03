from fastapi import FastAPI
from apiTools import *
from data import lista_clientes

app = FastAPI()


@app.get("/clientes")
async def get_clientes():
    return lista_clientes


@app.get("/clientes/{id}")
async def get_cliente_id(id: int):
    resposta = get_by_id(id, lista_clientes)
    return resposta


@app.post("/clientes-create")
async def create_cliente(nombre: str, plato_favorito: str):
    resposta = create_cliente_new(nombre, plato_favorito, lista_clientes)
    return resposta

@app.put("/clientes-update/{id}")
async def update_cliente(nombre: str, plato_favorito: str, id: int):
    resposta = update_cliente_by_id(nombre, plato_favorito, id, lista_clientes)
    return resposta
