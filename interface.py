from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')
layout = [
[sg.Text('Nome do titular'), sg.Input(key='Nome do titular')],
[sg.Text('Numero do cartão de credito'), sg.Input(key='Numero do cartão de credito')],
[sg.Text('CVV'), sg.Input(key='CVV')],
[sg.Button('Confirmar')]
]
janela=sg.Window('Cadastro de cartao', layout)
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break