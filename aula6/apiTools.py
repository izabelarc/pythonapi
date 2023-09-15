from datetime import date

def get_by_id(id, lista_clientes):
    for cliente in lista_clientes:
        if cliente["id"] == id:
            return cliente
    return "Não foi possível encontrar o cliente."

def create_cliente_new(nombre, plato_favorito, conta, lista_clientes: list):
    new_cliente = {
        "id": len(lista_clientes) + 1,
        "nombre": nombre,
        "plato_favorito": plato_favorito,
        "estrela": 1,
        "desconto_3_estrelas": 0,
        "vindas": [
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

def delete(id, lista_clientes):
    for index, cliente in enumerate(lista_clientes):
        if cliente["id"] == id:
            del lista_clientes[index]
            return lista_clientes

def contador_vindas(lista_clientes, id):
    for cliente in lista_clientes:
        if cliente["id"] == id:
            if len(cliente["vindas"]) >= 3:
                vindas = cliente["vindas"]
                ultima_vinda = vindas[-1]
                conta = ultima_vinda["conta"]
                total = (1 - 0.03) * conta
                cliente["desconto_3_estrelas"] = total
                return total
            else:
                falta = 3 - len(cliente["vindas"])
                return f"Faltam {falta} visitas para aplicar o desconto."

def new_conta(id, conta, lista_clientes):
    for cliente in lista_clientes:
        if cliente["id"] == id:
            cliente["vindas"].append({"data": date.today(), "conta": conta})
            cliente["estrela"] = len(cliente["vindas"])
    return lista_clientes

