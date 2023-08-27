from time import sleep


def fake_db() -> None:
    """
    Função criada para simular uma chamada async ao banco de dados
    """
    try:
        print("Abrindo conexão com banco de dados...")
        sleep(2)
    except:
        print("Fechando conexão com banco de dados...")
        sleep(2)
