import PySimpleGUI as sg

ROWS = COL = 8


layout = [
    [
        [
            sg.Button(
                " ",
                size=(8, 4),
                key=(i, j),
                pad=(0, 0),
            )
            for i in range(8)
        ]
        for j in range(8)
    ],
]


window = sg.Window("Xadrez", layout)

while True:
    event, values = window.read()
    print(event)
    if event in (None, "Exit"):
        break

window.close()
