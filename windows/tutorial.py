import PySimpleGUI as sg
import os

nome = None
txt_1 = '''Olá! meu nome é "Narrador" e estou aqui para te ajudar a jogar.
Como você é novo por aqui, vou te explicar como funciona o jogo.
Mas antes, me diga seu nome para que eu possa te chamar durante o jogo.'''

txt_2 = f'''Muito prazer, {nome}! Agora que já sei seu nome, vou te explicar onde você está e o que você precisa fazer.
Você está em Rio Negro, uma cidade conhecida por suas belezas naturais, rios e lagos repletos de peixes, desde os pequenos até peixes
considerados extintos pelos historiadores. Seu objetivo é se tornar o maior pescador de TODOS e sua jornada começa AQUI !
Chega de aprensentações, pega sua Vara (Lá Ele) e VAMOS NESSA !'''

def inicio():
    layout = [
        [sg.Text('Digite o nome do seu Personagem:', font=('Arial', 12))],
        [sg.Input(key='-NOME-', font=('Arial', 12))],
        []
    ]
