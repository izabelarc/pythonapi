lista_alunos = [
    {
        "id": 1,
        "nome": "Izabela"
    },
    {
        "id": 2,
        "nome": "Renato"
    }
]

# CRUD

# post
# criar uma função que coloca a aluna joana(letra minúscula) na lista
def post(lista, nome_aluna):
    novo_id = len(lista) + 1
    nova_aluna = {
        "id": novo_id,
        "nome": nome_aluna
    }
    lista.append(nova_aluna)

nome = input("Digite o nome que deseja inserir: ")
post(lista_alunos, nome)

#read
#criar uma função que leia todos os alunos e imprima
def read(a):
    return a

new_list = read(lista_alunos)
print(new_list)

#get
#criar uma função que leia por id o aluno e imprima
def encontra_nome(lista, aluno_id):
    for pessoa in lista:
        if pessoa["id"] == aluno_id:
            return pessoa["nome"]
    return None

digita = int(input("Digite o ID que deseja saber: "))
procura = encontra_nome(lista_alunos, digita)

if procura:
    print(f"Nome encontrado: {procura}")
else:
    print("Aluno não encontrado.")

#put
#criar uma função que atualiza a aluna joana na lista para Joana

def atualizar(lista, id_procurado, novo_nome):
    for pessoa in lista:
        if pessoa["id"] == id_procurado:
            pessoa["nome"] = novo_nome
            break
    return lista

id_procurado = int(input("Digite o id da pessoa que deseja alterar o nome: "))
novo_nome = input("Digite o novo nome: ")
nova_lista = atualizar(lista_alunos, id_procurado, novo_nome)

print(nova_lista)

#delete
#criar uma função que delete a joana

def delete(id: str):
    id_int = int(id)
    lista_alunos.pop(id_int-1)    
    return lista_alunos

id_deletado = int(input("Digite o id do aluno que deseja deletar: "))
delete(id_deletado)

print(lista_alunos)