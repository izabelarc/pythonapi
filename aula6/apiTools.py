from datetime import date

def get_by_id(id, lista_clientes):
    for cliente in lista_clientes:
        if cliente["id"] == id:
            return cliente
        else:
            return f"Não foi possível encontrar o cliente."


def create_cliente_new(nombre, plato_favorito, conta, lista_clientes: list):
    new_cliente = {
        "id": len(lista_clientes) + 1,
        "nombre": nombre,
        "plato_favorito": plato_favorito,
        "estrela": 1,
        "desconto_3_estrelas": 0, #valor da conta com desconto 3 por cento, quando ja tem 3 estrelas
        "vindas":[
                {
                     "data": date.today(),
                    "conta": conta,
                },
        ]
    }
    lista_clientes.append(new_cliente)
    return lista_clientes


def update_cliente_by_id(nombre, plato_favorito, id, lista_clientes):
    for cliente in lista_clientes:
        if cliente["id"] == id:
            cliente["nombre"] = nombre
            cliente["plato_favorito"] = plato_favorito

    return lista_clientes

def delete(id, nombre, plato_favorio, lista_clientes):
    if id in lista_clientes:
        del lista_clientes[id]
        new_lista = {}
       
        acc = 1
        for clientes_id in lista_clientes:
            new_lista[acc] = lista_clientes[clientes_id]
            acc += 1
        cursos = new_lista

def contador_vindas(lista_clientes,id):
    for i in lista_clientes:
        if i["id"] == id:
            if len(i["vindas"]) >= 3:
                vindas = i["vindas"]
                ultima_vinda = vindas[-1]
                conta = ultima_vinda["conta"]
                total =  (1-0.03)*conta
                return total
            else:
                falta = 3- len(i["vindas"])
                return f"Faltam {falta} visitas para aplicar o desconto."
            
def new_conta(id, conta, lista_clientes):
    for i in lista_clientes:
        if i["id"] == id:
            i["vindas"].append({"data":date.today(),"conta":conta})
    return lista_clientes
            # i["estrela"] = len(i["vindas"])
            # if len(i["vindas"]) >= 3:
            #     vindas = i["vindas"]
            #     ultima_vinda = vindas[-1]
            #     conta = ultima_vinda["conta"]
            #     total =  (1-0.03)*conta
            #     i["desconto_3_estrelas"] = total
            #     return lista_clientes
            # else:
            #     falta = 3- len(i["vindas"])
            #     return lista_clientes