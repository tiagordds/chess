import PySimpleGUI as sg

from buttons_notation import buttons_layout

ROWS = COL = 8


buttons_image = "empty_board.png"
layout = [buttons_layout]


window = sg.Window("Xadrez", layout)


while True:
    event, values = window.read()
    print(event)
    if event in (None, "Exit"):
        break
    elif event == "h7":
        window["h7"].update(button_color=("white"))

window.close()
