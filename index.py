import PySimpleGUI as sg
import os

from funcoes import login as login_module
from windows import login as win_module


# Busca os saves e cria a janela
saves = login_module.busca_save()
window = win_module.login(saves)


while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break

    # Carregar save
    elif event == '-LOAD-':

        selecionados = values['-TABELA-SAVES-']

        if not selecionados:
            sg.popup('Selecione um save na tabela.')
            continue

        indice = selecionados[0]
        caminho_save = saves[indice]['arquivo']

        print('Save selecionado:', caminho_save)

        # Futuramente:
        # dados = login_module.importar_save(caminho_save)
        # Abrir a tela do jogo com os dados carregados.

    # Excluir save
    elif event == '-DELETE-':

        selecionados = values['-TABELA-SAVES-']

        if not selecionados:
            sg.popup('Selecione um save na tabela para excluir.')
            continue

        indice = selecionados[0]
        save_selecionado = saves[indice]
        caminho_save = save_selecionado['arquivo']

        confirmacao = sg.popup_yes_no(
            f'Deseja realmente excluir o save de '
            f'"{save_selecionado["jogador"]}" '
            f'do dia {save_selecionado["data"]}?'
        )

        if confirmacao == 'Yes':

            try:
                os.remove(caminho_save)

                sg.popup('Save excluído com sucesso.')

                # Atualiza a lista de saves
                saves = login_module.busca_save()

                # Atualiza os dados exibidos na tabela
                dados_tabela = [
                    [save['jogador'], save['data']]
                    for save in saves
                ]

                window['-TABELA-SAVES-'].update(
                    values=dados_tabela
                )

            except OSError as erro:
                sg.popup(f'Erro ao excluir o save: {erro}')

    # Criar novo save
    elif event == '-NEW-':

        print('Criar novo save')

    # Login
    elif event == 'Login':

        print('Realizar login')


window.close()
