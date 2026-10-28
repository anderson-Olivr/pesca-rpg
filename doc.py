import random
import time
import os

nome = input("Digite seu nome: ")

documento = f'save/save-{nome}-{int(time.time())}.csv'

with open(documento, "w", encoding="utf-8") as file:
    file.write(f"Ola meu nome é {nome}")
    file.write("\n")
#def start(name):

escolha = input('Deseja Listar os arquivos salvos? (s/n): ')
if escolha == 's':
    print("Listando arquivos salvos...")
    time.sleep(1)
    arquivos = os.listdir()
    for arquivo in arquivos:
        if arquivo.startswith('save-') and arquivo.endswith('.txt'):
            print(arquivo)

escola = input('Deseja abrir algum arquivo? (s/n): ')
if escola == 's':
    arquivo_escolhido = input('Digite o nome do arquivo que deseja abrir: ')
    documento = f'save-{arquivo_escolhido}.txt'
    if os.path.exists(documento):
        with open(documento, "r", encoding="utf-8") as file:
            conteudo = file.read()
            print(f"Conteúdo do arquivo {arquivo_escolhido}:")
            print(conteudo)
    else:
        print("Arquivo não encontrado.")