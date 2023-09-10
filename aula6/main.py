from fastapi import FastAPI, HTTPException, status, Path
from apiTools import *
from data import lista_clientes

app = FastAPI()

# Traz a lista de clientes completa
@app.get("/clientes", status_code=status.HTTP_200_OK)
async def get_clientes():
    try:
        return lista_clientes
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Clientes não encontrados"
        )


#Traz cliente através da busca pelo id
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

#Traz cliente através da busca pelo id usando Path
@app.get('/cliente/{id}', status_code=status.HTTP_200_OK)
async def get_cliente_id(id: int = Path(
    title='ID do curso',
    description=f'Deve ser de 1 a {len(lista_clientes)}',
    gt=1,
    lt=len(lista_clientes) + 1)
    ):
    try:
        resposta = get_by_id(id, lista_clientes)
        return resposta
    except:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Cliente não encontrado'
        )

#Cria um novo cliente
@app.post("/clientes-create", status_code=status.HTTP_201_CREATED)
async def create_cliente(nombre: str, plato_favorito: str, conta:float):
    try:
        resposta = create_cliente_new(nombre, plato_favorito, conta, lista_clientes)
        return resposta
    except:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Não foi possível criar o cliente."
        )
  
#Atualiza os dados de um cliente      
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

#Deleta um cliente e seus dados e atualiza o id dos outros que ficaram
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


@app.get("/vindas/{id}", status_code=status.HTTP_200_OK)
async def get_conta(id:int):
    try:
        resposta = contador_vindas(lista_clientes, id)
        return resposta
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não foi possível encontrar o número de vindas desse cliente"
        )


@app.get("/conta/{id}", status_code=status.HTTP_102_PROCESSING) 
async def get_conta(id: int, conta: int):
    try:
        resposta = new_conta(id)
        return resposta
        
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Não foi possível gerar a conta do cliente."
        )