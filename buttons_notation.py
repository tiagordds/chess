import PySimpleGUI as sg

BUTTON_COLOR_LIGHT = "LightGrey"
BUTTON_COLOR_DARK = "Grey"
BUTTON_SIZE = (8, 4)
square_notation = [
    "a8",
    "b8",
    "c8",
    "d8",
    "e8",
    "f8",
    "g8",
    "h8",
    "a7",
    "b7",
    "c7",
    "d7",
    "e7",
    "f7",
    "g7",
    "h7",
    "a6",
    "b6",
    "c6",
    "d6",
    "e6",
    "f6",
    "g6",
    "h6",
    "a5",
    "b5",
    "c5",
    "d5",
    "e5",
    "f5",
    "g5",
    "h5",
    "a4",
    "b4",
    "c4",
    "d4",
    "e4",
    "f4",
    "g4",
    "h4",
    "a3",
    "b3",
    "c3",
    "d3",
    "e3",
    "f3",
    "g3",
    "h3",
    "a2",
    "b2",
    "c2",
    "d2",
    "e2",
    "f2",
    "g2",
    "h2",
    "a1",
    "b1",
    "c1",
    "d1",
    "e1",
    "f1",
    "g1",
    "h1",
]

buttons_layout = [
    # 8 LINE
    [
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[0]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[1]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[2]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[3]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[4]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[5]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[6]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[7]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
    ],
    # 7 LINE
    [
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[8]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[9]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[10]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[11]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[12]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[13]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[14]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[15]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
    ],
    # 6 LINE
    [
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[16]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[17]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[18]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[19]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[20]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[21]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[22]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[23]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
    ],
    # 5 LINE
    [
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[24]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[25]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[26]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[27]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[28]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[29]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[30]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[31]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
    ],
    # 4 LINE
    [
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[32]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[33]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[34]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[35]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[36]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[37]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[38]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[39]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
    ],
    # 3 LINE
    [
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[40]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[41]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[42]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[43]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[44]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[45]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[46]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[47]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
    ],
    # 2 LINE
    [
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[48]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[49]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[50]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[51]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[52]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[53]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[54]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[55]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
    ],
    # 1 LINE
    [
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[56]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[57]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[58]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[59]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[60]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[61]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[62]),
            button_color=BUTTON_COLOR_DARK,
            pad=(0, 0),
        ),
        sg.Button(
            "",
            size=(BUTTON_SIZE),
            key=(square_notation[63]),
            button_color=BUTTON_COLOR_LIGHT,
            pad=(0, 0),
        ),
    ],
]