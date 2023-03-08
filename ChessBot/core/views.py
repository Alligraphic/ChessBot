from django.shortcuts import render

import ChessBot.core.helper_functions as hf


def index(request):
    fen_str = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    chess_matrix = hf.fen_to_matrix(fen_str)
    board_color = hf.generate_board()
    # initialize the dict
    board = []
    for i in range(64):
        board.append({"color": board_color[i], "piece": chess_matrix[i]})
        # add id to each piece
        if board[i]["piece"] != "":
            board[i]["id"] = board[i]["piece"][1] + str(i)
    return render(request, "board.html", {'board': board})

