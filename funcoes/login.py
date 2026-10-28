
import os
from datetime import datetime

# Caminho absoluto da pasta save, que fica junto de index.py
PASTA_SAVE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'save')


def busca_save():
    """
    Retorna uma lista de saves contendo:
    jogador, data, data_objeto e caminho do arquivo.
    """

    saves = []

    # Cria a pasta caso ela ainda não exista
    os.makedirs(PASTA_SAVE, exist_ok=True)

    try:
        arquivos = os.listdir(PASTA_SAVE)
    except OSError as erro:
        print(f'Erro ao acessar a pasta de saves: {erro}')
        return saves

    for arquivo in arquivos:

        # Aceita somente arquivos CSV com prefixo save-
        if not arquivo.startswith('save-') or not arquivo.endswith('.csv'):
            continue

        # Remove o prefixo e a extensão
        nome_arquivo = arquivo[5:-4]

        # Separa o nome do jogador da data
        partes = nome_arquivo.rsplit('-', 3)

        if len(partes) != 4:
            print(f'Nome de save inválido: {arquivo}')
            continue

        nome_jogador = partes[0]
        data = '-'.join(partes[1:])

        # Confere se a data é válida
        try:
            data_objeto = datetime.strptime(data, '%d-%m-%Y')
        except ValueError:
            print(f'Data inválida no arquivo: {arquivo}')
            continue

        # Guarda os dados do save
        saves.append({
            'jogador': nome_jogador,
            'data': data,
            'data_objeto': data_objeto,
            'arquivo': os.path.join(PASTA_SAVE, arquivo)
        })

    # Ordena do mais recente para o mais antigo
    saves.sort(
        key=lambda save: save['data_objeto'],
        reverse=True
    )

    return saves