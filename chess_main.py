import PySimpleGUI as sg

pieces_initial_positions = {
    (0, 0): "W_Rook",
    (0, 1): "W_Knight",
    (0, 3): "W_Bishop",
    (0, 4): "W_Queen",
    (0, 5): "W_King",
    (0, 6): "W_Bishop",
    (0, 7): "W_Knight",
    (0, 8): "W_Rook",
}


def create_chessboard():
    board = []
    for row in range(72, 64, -1):
        row_layout = []
        for col in range(1, 9):
            square_color = "gray" if (row + col) % 2 == 0 else "white"
            row_layout.append(
                sg.Button(
                    "",
                    size=(10, 5),
                    key=((col), chr(row)),
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
