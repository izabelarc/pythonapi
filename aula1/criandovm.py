"""
ESTRUTURA DE URL:
    https - s garante a segurança da transação de dados
    dominio - nome do site
    indicações/endpoints - exemplo de pastas e subpastas de onde está a aplicação

TERMINAL
cd .\fastapi\ - muda diretorio para a pasta que quer
cls - limpa o terminal
python -m venv env - cria um ambiente virtual chamado env com scripts que ativam o ambiente
 Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned - comando para rodar no powershell sem ser adm 
 e em seguida colocar A(Sim para todos)
 .\env\Scripts\activate - ativa a máquina virtual
 cd .\env\ - entra na pasta env
 pip install jinja2  - instala o jinja
 pip install python-multipart
 pip install fastapi uvicorn - instala o CRUD
 uvicorn main:app --reload - dentro da pasta que tem o main e dentro do env pára rodar

 VAI ABRIR http://127.0.0.1:8000 e é só colocar o /(nome)

CRUD (4 operações básicas)
    create - cria uma nova instância/dado
    read - ler da forma simples ou completa, preferencial simples
    update - atualizar dado
    delete - remover dado
    HTTP faz com o rest - CRUD DO REST
        GET
        POST
        PUT
        DELETE
"""
#@app faz parte do anotations, dão superpoderes para as variaveis que é o app