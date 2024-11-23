import PySimpleGUI as sg


def create_chessboard():
    board = []
    unicode_conveter = [72, 71, 70, 69, 68, 67, 66, 65]
    for row in unicode_conveter:
        row_layout = []
        for col in range(8):
            square_color = "white" if (row + col) % 2 == 0 else "gray"
            row_layout.append(
                sg.Button(
                    "",
                    size=(10, 5),
                    key=((col + 1), chr(row)),
                    button_color=("black", square_color),
                )
            )
        board.append(row_layout)
    return board


layout = create_chessboard()
window = sg.Window("First Chess Game", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    print(f"Clicked on square: {event}")

window.close()
