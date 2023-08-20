<<<<<<< HEAD
cursos = {
    1: {
        "titulo": "Programação para leigos",
        "aulas": 112,
        "horas": 58,
    },
    2: {
        "titulo": "Algoritmos e lógica de programação",
        "aulas": 87,
        "horas": 67,
    },
}

# get {1: {'titulo': 'Programação para leigos', 'aulas': 112, 'horas': 58}, 2: {'titulo': 'Algoritmos e lógica de programação', 'aulas': 87, 'horas': 67}}
print(cursos)

# post
# {1: {'titulo': 'Programação para leigos', 'aulas': 112, 'horas': 58}, 2: {'titulo': 'Algoritmos e lógica de programação', 'aulas': 87, 'horas': 67},
#  3: {'titulo': 'teste', 'aulas': 555, 'horas': 4444}}
titulo = "teste"
aulas = 555
horas = 4444
next_id: int = len(cursos) + 1
cursos[next_id] = {
    "titulo": titulo,
    "aulas": aulas,
    "horas": horas,
}

print(cursos)

# update
# {1: {'titulo': 'teste', 'aulas': 333, 'horas': 222}, 2: {'titulo': 'Algoritmos e lógica de programação', 'aulas': 87, 'horas': 67},
# 3: {'titulo': 'teste', 'aulas': 555, 'horas': 4444}}
id = 1
titulo = "teste"
aulas = 333
horas = 222

if id in cursos:
    cursos[id] = {
        "titulo": titulo,
        "aulas": aulas,
        "horas": horas,
    }

print(cursos)

#  delete
#  {1: {'titulo': 'teste', 'aulas': 333, 'horas': 222}, 2: {'titulo': 'teste', 'aulas': 555, 'horas': 4444}}
id = 2
if id in cursos:
    del cursos[id]  # del ....estudem depois
    new_cursos = {}
    # Atualizando ids
    acc = 1
    for curso_id in cursos:
        new_cursos[acc] = cursos[curso_id]
        acc += 1
    cursos = new_cursos

print(cursos)
=======
cursos = {
    1: {
        "titulo": "Programação para leigos",
        "aulas": 112,
        "horas": 58,
    },
    2: {
        "titulo": "Algoritmos e lógica de programação",
        "aulas": 87,
        "horas": 67,
    },
}

# get {1: {'titulo': 'Programação para leigos', 'aulas': 112, 'horas': 58}, 2: {'titulo': 'Algoritmos e lógica de programação', 'aulas': 87, 'horas': 67}}
print(cursos)

# post
# {1: {'titulo': 'Programação para leigos', 'aulas': 112, 'horas': 58}, 2: {'titulo': 'Algoritmos e lógica de programação', 'aulas': 87, 'horas': 67},
#  3: {'titulo': 'teste', 'aulas': 555, 'horas': 4444}}
titulo = "teste"
aulas = 555
horas = 4444
next_id: int = len(cursos) + 1
cursos[next_id] = {
    "titulo": titulo,
    "aulas": aulas,
    "horas": horas,
}

print(cursos)

# update
# {1: {'titulo': 'teste', 'aulas': 333, 'horas': 222}, 2: {'titulo': 'Algoritmos e lógica de programação', 'aulas': 87, 'horas': 67},
# 3: {'titulo': 'teste', 'aulas': 555, 'horas': 4444}}
id = 1
titulo = "teste"
aulas = 333
horas = 222

if id in cursos:
    cursos[id] = {
        "titulo": titulo,
        "aulas": aulas,
        "horas": horas,
    }

print(cursos)

#  delete
#  {1: {'titulo': 'teste', 'aulas': 333, 'horas': 222}, 2: {'titulo': 'teste', 'aulas': 555, 'horas': 4444}}
id = 2
if id in cursos:
    del cursos[id]  # del ....estudem depois
    new_cursos = {}
    # Atualizando ids
    acc = 1
    for curso_id in cursos:
        new_cursos[acc] = cursos[curso_id]
        acc += 1
    cursos = new_cursos

print(cursos)
>>>>>>> ef4ed64e96c0647aa1fee3916d0a9aba4d1c45f5
