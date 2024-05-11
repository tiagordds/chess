import PySimpleGUI as sg

layout = [
    [sg.Text(text="OLHA ISSO")],
    [sg.Image("board.png")],
]

window = sg.Window("Xadrez marotão", layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (None, "Exit"):
        break

window.close()
