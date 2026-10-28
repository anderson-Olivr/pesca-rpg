import PySimpleGUI as sg

# Padronização das cores e fontes
sg.theme('DarkGrey5')
font = ('Arial', 12)


def login(saves):

    dados_tabela = [
        [save['jogador'], save['data']]
        for save in saves
    ]

    layout = [
        [
            sg.Text(
                'Selecione um save para continuar:',
                font=font
            )
        ],
        [
            sg.Table(
                values=dados_tabela,
                headings=['Jogador', 'Data do save'],
                key='-TABELA-SAVES-',
                font=font,
                auto_size_columns=False,
                col_widths=[20, 15],
                justification='left',
                num_rows=8,
                select_mode=sg.TABLE_SELECT_MODE_BROWSE,
                expand_x=True,
                expand_y=True
            )
        ],
        [
            sg.Button(
                'Carregar Save',
                key='-LOAD-',
                font=font,
                button_color=('white', '#4CAF50')
            ),
            sg.Button(
                'Novo Save',
                key='-NEW-',
                font=font,
                button_color=('white', '#2196F3')
            ),
            sg.Button(
                'Excluir',
                key='-DELETE-',
                font=font,
                button_color=('white', '#f44336')
            )
        ],
        [
            sg.Button('Login', font=font, button_color=('white', '#2196F3')),
            sg.Button('Cancelar', font=font, button_color=('white', '#f44336'))
        ]
    ]

    return sg.Window('Login', layout, finalize=True)

