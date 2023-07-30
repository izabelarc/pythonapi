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
def post(a):
    insere =  lista_alunos.append({"id: ": len(lista_alunos) + 1, "nome: ": a})
    return insere

nome = input("Digite o nome que deseja inserir: ")
post(nome)

#read
#criar uma função que leia todos os alunos e imprima
def read(a):
    return a

new_list = read(lista_alunos)
print(new_list)

#get
#criar uma função que leia por id o aluno e imprima
def encontra_nome(lista, id: int):
    for pessoa in lista:
        if pessoa["id"] == id:
            return pessoa["nome"]

digita = int(input("Digite o id que deseja saber: "))
procura = encontra_nome(new_list, digita)
print(procura)

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
nova_lista = atualizar(new_list, id_procurado, novo_nome)

print(nova_lista)


#delete
#criar uma função que delete a joana