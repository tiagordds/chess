import PySimpleGUI as sg

pieces_initial_positions = {
    (0, 0): "♜",
    (1, 0): "♞",
    (2, 0): "♝",
    (3, 0): "♛",
    (4, 0): "♚",
    (5, 0): "♝",
    (6, 0): "♞",
    (7, 0): "♜",
    (0, 1): "♟",
    (1, 1): "♟",
    (2, 1): "♟",
    (3, 1): "♟",
    (4, 1): "♟",
    (5, 1): "♟",
    (6, 1): "♟",
    (7, 1): "♟",
    (0, 7): "♖",
    (1, 7): "♘",
    (2, 7): "♗",
    (3, 7): "♕",
    (4, 7): "♔",
    (5, 7): "♗",
    (6, 7): "♘",
    (7, 7): "♖",
    (0, 6): "♙",
    (1, 6): "♙",
    (2, 6): "♙",
    (3, 6): "♙",
    (4, 6): "♙",
    (5, 6): "♙",
    (6, 6): "♙",
    (7, 6): "♙",
}


def create_chessboard():
    board = []
    for line in range(8):
        line_layout = []
        for col in range(8):
            square_color = "white" if (line + col) % 2 == 0 else "gray"
            if (col, line) in pieces_initial_positions.keys():
                line_layout.append(
                    sg.Button(
                        pieces_initial_positions[col, line],
                        size=(10, 5),
                        key=(col, line),
                        button_color=("black", square_color),
                        font=("Arial", 13),
                        auto_size_button=False,
                    )
                )
            else:
                line_layout.append(
                    sg.Button(
                        "",
                        size=(10, 5),
                        key=(col, line),
                        font=("Arial", 13),
                        auto_size_button=False,
                        button_color=("black", square_color),
                    )
                )
        board.append(line_layout)
    return board


layout = create_chessboard()
window = sg.Window("First Chess Game", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    print(f"Clicked on square: {event}")

window.close()
