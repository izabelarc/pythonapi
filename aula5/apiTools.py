def get_by_id(id, lista_clientes):
    for cliente in lista_clientes:
        if cliente["id"] == id:
            return cliente


def create_cliente_new(nombre, plato_favorito, lista_clientes: list):
    new_cliente = {
        "id": len(lista_clientes) + 1,
        "nombre": nombre,
        "plato_favorito": plato_favorito,
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
