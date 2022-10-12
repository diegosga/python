from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')
layout = [
[sg.Text('Nome'), sg.Input(key='Nome')],
[sg.Text('Numero de Telefone'), sg.Input(key='Numero de Telefone')],
[sg.Text('Email'), sg.Input(key='Email')],
[sg.Text('Senha'), sg.Input(key='Senha')],
[sg.Text('Digite a senha novamente'), sg.Input(key='Digite a senha novamente')],
[sg.Button('Confirmar')]
]
janela=sg.Window('Cadastro', layout)
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
