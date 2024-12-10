import PySimpleGUI as sg

# Chess_adt45 = b"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"
# wR = b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAMAAAAp4XiDAAAAAXNSR0IB2cksfwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAWtQTFRFAAAAEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQISEhj4+PnZ2dOTk5bW1tEBAQJycn2dnZ+fn5VFRUqampEBAQIiIizs7OEBAQEBAQEBAQEBAQHBwcw8PDWFhYFRUVq6urEBAQFhYWuLi4EBAQERERra2tEBAQODg41NTUEBAQEBAQlZWVEBAQEBAQEBAQXFxcoKCgoqKiXV1dEBAQEREREBAQEBAQEBAQEBAQEBAQgoKChYWFNzc39/f3EBAQEBAQSEhIEBAQEBAQX19fEBAQdHR0EBAQi4uLEBAQs7OzwcHBEBAQ0NDQEBAQ39/fEBAQ7e3tEBAQExMT+Pj4EBAQEBAQKysr2traEBAQFxcXEBAQEBAQEBAQSkpKbGxsEBAQEBAQEBAQGxsbgYGB6+vrEBAQEBAQLi4uqqqqEBAQEBAQ3NzcEBAQEBAQZ2dnEBAQfHx8EBAQEBAQKioqPDw8EBAQEBAQEBAQ7CyG4gAAAHl0Uk5TAEBLDCTS/yt7yP//////vP//////sv//xrrbp///////nP//kf//g///GKH/BVnp/////1oAN+0AEeX/////IfX/Kv3/OP9J/2v//5D/qv/D/9r///MJ//8m/wFV4P//Donw////B6z//xfs/yP3/zn/W4H//6ILEHiCQVMAAAI8SURBVHic7dXfT85RHAfwz/vRo8dSxjIbF62m4UHJZDWziCSZRcMw8+PCRWTGxt/gotZEFy78mGFYNJMkopn1DJNKYazWBZtpTE/meTzp4zzHt833nPM948ZceF+d89l57XzPPuf7/YL+OPhP/i7Bzwm+U8KoHPlGaBzLEbOZ+B0SpYBDIpTokJiZTIDYB1FJBPJFJBGImb+aySRJwpKkCDIkSbIkn81kKhATZIpwg5KkitUfBfGHkz6YyQzgC010DjREKc4xhimJ+a2ZpAOfyJTJzP1mMhMYNJJU5jdmMqs/A+8NYhr3pb8ykyBeJ2S808T0vpFM7jUTmg+8CMJ9h9jXPccf7SYPQrlAh7ZLDvtCv86Va5mPZznKLh0LuN1VUUgweTyeuyrz+Fu411VRSAHQqTxXNnObjRQCTxWykLnVRoralj1RyKL7BS02Unyv8JFCFrcub7aRrJdzBxSS1jO7y0ZK7q4MuSuUd2dFk40ERovcTRCtahFvmoWsvV38UCFLmlfdsJF1t0oeKGRp0+rrNlJ2s9TdN9HdxjUNNrIBcPdNdJf5qo1sbAyQmkjpFQvZ1LBe/+LytbLL3mRLfVquRh4PlF/0ItuAUL5hl/Y85vNGshPx1GuknOM5YyB7cHo3Lmkgns18ahef1EkFurIvGAXR1s4srtNJJXDOQxBtZ67VyYG6vWc9yY4TFTU6OXjcn+hJorF91To5VLvf+8fJxyqrdHK4xrh4LJk9Ojli/znzUZ38dv5Z8gOK7L8zIEj8+QAAAABJRU5ErkJggg=="

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


def create_chessboard():
    board = []
    for line in range(8, 0, -1):
        line_layout = []
        for col in range(65, 73):
            square_color = "gray" if (line + col) % 2 == 0 else "white"
            if (col, line) in pieces_initial_positions.keys():
                line_layout.append(
                    sg.Button(
                        "",
                        image_data=pieces_initial_positions[col, line],
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
                        key=(chr(col), line),
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
