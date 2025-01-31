import PySimpleGUI as sg

pieces_initial_positions = {
    (65, 8): "♜",
    (66, 8): "♞",
    (67, 8): "♝",
    (68, 8): "♛",
    (69, 8): "♚",
    (70, 8): "♝",
    (71, 8): "♞",
    (72, 8): "♜",
    (65, 7): "♟",
    (66, 7): "♟",
    (67, 7): "♟",
    (68, 7): "♟",
    (69, 7): "♟",
    (70, 7): "♟",
    (71, 7): "♟",
    (72, 7): "♟",
    (65, 1): "♖",
    (66, 1): "♘",
    (67, 1): "♗",
    (68, 1): "♕",
    (69, 1): "♔",
    (70, 1): "♗",
    (71, 1): "♘",
    (72, 1): "♖",
    (65, 2): "♙",
    (66, 2): "♙",
    (67, 2): "♙",
    (68, 2): "♙",
    (69, 2): "♙",
    (70, 2): "♙",
    (71, 2): "♙",
    (72, 2): "♙",
}

piece_ownership = {
    "♙": "White",
    "♖": "White",
    "♘": "White",
    "♗": "White",
    "♕": "White",
    "♔": "White",
    "♟": "Black",
    "♜": "Black",
    "♞": "Black",
    "♝": "Black",
    "♛": "Black",
    "♚": "Black",
}


def get_piece_type(piece):
    pieces = {
        "♙": "pawn",
        "♟": "pawn",
        "♖": "rook",
        "♜": "rook",
        "♘": "knight",
        "♞": "knight",
        "♗": "bishop",
        "♝": "bishop",
        "♕": "queen",
        "♛": "queen",
        "♔": "king",
        "♚": "king",
    }
    return pieces.get(piece)


def is_valid_pawn_move(source, target, piece, piece_positions):
    source_col, source_row = source
    target_col, target_row = target
    direction = 1 if piece == "♙" else -1

    # basic move foward
    if source_col == target_col and target_row == source_row + direction:
        return target not in piece_positions

    # checks if it's the first pawn move
    if (source_row == 2 and piece == "♙") or (source_row == 7 and piece == "♟"):
        if source_col == target_col and target_row == source_row + 2 * direction:
            intermediate_square = (source_col, source_row + direction)
            return (
                target not in piece_positions
                and intermediate_square not in piece_positions
            )

    # capture move
    if abs(source_col - target_col) == 1 and target_row == source_row + direction:
        return target in piece_positions
    return False


def is_valid_move(source, target, piece, pieces_positions):
    piece_type = get_piece_type(piece)
    if piece_type == "pawn":
        return is_valid_pawn_move(source, target, piece, pieces_positions)

    return False


def create_chessboard():
    board = []
    for line in range(8, 0, -1):
        line_layout = []
        for col in range(65, 73):
            square_color = "gray" if (line + col) % 2 == 0 else "white"
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

selected_square = None
current_player = "White"

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    print(f"Clicked on square: {event}")
    if selected_square is None:
        selected_square = event
    else:
        source_piece = pieces_initial_positions.get(selected_square)

        if source_piece:
            if piece_ownership.get(source_piece) == current_player:
                if is_valid_move(
                    selected_square, event, source_piece, pieces_initial_positions
                ):
                    window[selected_square].update("")
                    window[event].update(source_piece)

                    pieces_initial_positions[event] = source_piece
                    del pieces_initial_positions[selected_square]

                    current_player = "Black" if current_player == "White" else "White"
                    print(f"It's now {current_player}'s turn.")
            selected_square = None
        else:
            print("Invalid move. Try again.")


window.close()
