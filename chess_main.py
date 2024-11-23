import PySimpleGUI as sg

pieces_initial_positions = {
    (0, 0): "B_Rook",
    (1, 0): "B_Knight",
    (2, 0): "B_Bishop",
    (3, 0): "B_Queen",
    (4, 0): "B_King",
    (5, 0): "B_Bishop",
    (6, 0): "B_Knight",
    (7, 0): "B_Rook",
    (0, 1): "B_Pawn",
    (1, 1): "B_Pawn",
    (2, 1): "B_Pawn",
    (3, 1): "B_Pawn",
    (4, 1): "B_Pawn",
    (5, 1): "B_Pawn",
    (6, 1): "B_Pawn",
    (7, 1): "B_Pawn",
    (0, 7): "W_Rook",
    (1, 7): "W_Knight",
    (2, 7): "W_Bishop",
    (3, 7): "W_Queen",
    (4, 7): "W_King",
    (5, 7): "W_Bishop",
    (6, 7): "W_Knight",
    (7, 7): "W_Rook",
    (0, 6): "W_Pawn",
    (1, 6): "W_Pawn",
    (2, 6): "W_Pawn",
    (3, 6): "W_Pawn",
    (4, 6): "W_Pawn",
    (5, 6): "W_Pawn",
    (6, 6): "W_Pawn",
    (7, 6): "W_Pawn",
}


def create_chessboard():
    board = []
    for row in range(8):
        row_layout = []
        for col in range(8):
            square_color = "white" if (row + col) % 2 == 0 else "gray"
            row_layout.append(
                sg.Button(
                    "",
                    size=(10, 5),
                    key=((col), row),
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
