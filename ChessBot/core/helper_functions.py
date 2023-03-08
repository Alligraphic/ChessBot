# coverts fen string to matrix
def fen_to_matrix(fen):
    board = []
    for row in fen.split("/"):
        for piece in row:
            if piece.isdigit():
                board.extend([""] * int(piece))
            else:
                if piece.isupper():
                    board.append(f'w{piece.lower()}')
                else:
                    board.append(f'b{piece}')
    return board


# generate an 8*8 matrix of black and white squares
def generate_board():
    board = []
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 1:
                board.append("white")
            else:
                board.append("black")
    return board
