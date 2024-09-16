import chess

# Create a new chess board
board = chess.Board()
squares = [
    "a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8",
    "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7",
    "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6",
    "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5",
    "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4",
    "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3",
    "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",
    "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"
]

algoQ = [9, 18, 27, 36, 45, 54, 63,
         8, 16, 24, 32, 40, 48, 56,
         7, 14, 21, 28, 35, 42, 49, 56,
         -1, -2, -3, -4, -5, -6, -7,
         -9, 18, -27, -36, -45, -54, -63,
         -8, -16, -24, -32, -40, -48, -56,
         -7, -14, -21, -28, -35, -42, -49, -56,
         1, 2, 3, 4, 5, 6, 7, 9]
algoK = [9, 8, 7, -1, -9, -8, -7, 1]
algoN = [10, 17, 15, 6, -10, -17, -15, -6]
algoP = [8, 16, 9, 7, -8, -16, -9, -7]
algoB = [9, 18, 27, 36, 45, 54, 63, 7, 14, 21, 28, 35, 42, 49, 56, -9,
         18, -27, -36, -45, -54, -63, -7, -14, -21, -28, -35, -42, -49, -56,]
algoR = [8, 16, 24, 32, 40, 48, 56, -1, -2, -3, -4, -5, -6, -
         7, -8, -16, -24, -32, -40, -48, -56, 1, 2, 3, 4, 5, 6, 7, 9]

algo2 = ['n', 'b', 'r', 'q']

ar = [
    "Kb8,Kc8,Kd8,Kd7,Kd6,Kb6,Bg4,Bf5,Be6,Bd7,Bc8,Bg2,Bf1",
    "Qb5,Qa6,Qc5+,Qc6+,Qxc7,Qd5,Qe6,Qf7+,Qg8,Qd4,Qe4,Qf4+,Qg4,Qh4,Qd3,Qc3+,Qc2+,Qc1+,Qb3,Qa2,Qb4,Qa4,Kd3+,Kf2+,Ke1+,Kd2+",
    "a3,a4,b3,b4,c3,c4,d3,d4,e3,e4,f3,f4,g3,g4,h3,h4,Na3,Nc3,Nf3,Nh3",
    "b5,a3,a4,c3,c4,d3,d4,e3,e4,f3,f4,g3,g4,h3,h4,Na3,Nc3,Bb2,Ba3,Nf3,Nh3",
    "Ne5,Ng5,Nh4,Ng1,Nfd2,a3,a4,b3,b4,c3,c4,e3,e4,g3,h3,h4,Na3,Nc3,Nbd2,Bd2,Be3,Bf4,Bg5,Bh6,Qd2,Qd3,Kd2,Rg1",
    "a3,a4,b3,b4,c3,c4,e3,e4,f3,f4,g3,h3,h4,Na3,Nc3,Nd2,Bd2,Be3,Bf4,Bg5,Bh6,Qd2,Qd3,Kd2,Rg1",
    "Nd7,Nc6,Na6,Qd7,Qd6,Qc8,Kd7,Nh6,Nf6,Rh7,Rh6,Rh5,Rxh4,a6,a5,b6,b5,c6,c5,e6,e5,f6,f5,g6,g5,g3,gxh3",
    "a3,a4,b3,b4,c3,c4,e3,e4,f3,f4,g3,g4,gxh3,Na3,Nc3,Nd2,Bd2,Be3,Bf4,Bg5,Bh6,Qd2,Qd3,Kd2,Rh2,Rxh3,Rg1",
    "Nd7,Nc6,Na6,Qd7,Qd6,Qc8,Kd7,Nh6,Nf6,a6,a5,b6,b5,c6,c5,e6,e5,f6,f5,g6,g5,dxc4,g1=N,g1=B,g1=R,g1=Q,gxf1=N,gxf1=B,gxf1=R+,gxf1=Q+",
    "Rb8,Rc8,Rd8,Re8,Kg8,Ke8,a6,a5,b6,b5,c6,c5,Qc8,Qd8,Qe8,Qe6,Qdf5,Qg4,Qdh3,Qd6,Qd5,Qxd4,Qc6,Qb5,Qa4,e6,e5,f6,f5,g6,g5,Qg8,Qh8,Qh6,Qh5,Qh4,Qhh3,Qh2,Qh1+,Qg6,Qhf5,Qe4,Qd3,Qc2,Qb1,Na6,Nc6,Nd5,Nd3+,Nc2+,Nxa2",
    "d6,dxc6,a3,a4,b3,b4,c3,c4,e3,e4,f3,f4,g3,g4,h3,h4,Na3,Nc3,Nd2,Bd2,Be3,Bf4,Bg5,Bh6,Qd2,Qd3,Qd4,Kd2,Nf3,Nh3",
    "b8=N,b8=B,b8=R,b8=Q,bxa8=N,bxa8=B,bxa8=R,bxa8=Q,bxc8=N,bxc8=B,bxc8=R,bxc8=Q,d6,dxc6,e5,b3,b4,c3,c4,f3,f4,g3,g4,h3,h4,Ra2,Ra3,Ra4,Ra5,Rxa6,Na3,Nc3,Nd2,Bd2,Be3,Bf4,Bg5,Bh6,Qd2,Qd3,Qd4,Qe2,Qf3,Qg4,Qh5,Kd2,Ke2,Be2,Bd3,Bc4,Bb5,Bxa6,Ne2,Nf3,Nh3",
    "d6,e5,Nd4,Ne5,Ng5,Nh4,Ng1,Nfd2,b3,b4,c3,c4,Bd3,Bc4,Bb5,Bxa6,Bf1,g3,g4,h3,h4,Ra2,Ra3,Ra4,Rxa5,Na3,Nc3,Nbd2,Bd2,Be3,Bf4,Bg5,Bh6,Qd2,Qd3,Qd4,Kd2,Kf1,Rg1,Rf1,O-O",
    "Rb8,Rc8,Rd8,Ra7,Kf8,Kd8,Rg8,Rf8,Bc8,Bc6,Bxd5,Qb8,Qc8,Qd8,Qd6,Qe5,Qf4,Qg3,Qxh2,Qc6,Qb6,d6,e6,e5,Bf8,Bh6,h6,h5,Ng8,Nh5,Ng4,Nxe4,Nxd5,g5,Nc6,Nc4,Nxb3,c4,O-O,O-O-O",
    "e5,b4,Na4,Nb5,Nd1,Nb1,Na2,Nd4,Ne5,Ng5,Nxh4,Ng1,Ba3,Bc1,Qd3,Qd4,Qe3,Qf4,Qg5,Qh6,Qd1,Qc1,Bd3,Bc4,Bb5+,Bxa6,Bf1,Bd1,g3,g4,h3,Ra2,Ra3,Ra4,Rxa5,Rb1,Rc1,Rd1,Kf1,Kd1,Rg1,Rf1,O-O,O-O-O",
    "e5,b4,Na4,Nb5,Nd1,Nb1,Na2,Nd4,Ne5,Ng5,Nxh4,Ng1,Ba3,Bc1,Qd3,Qd4,Qe3,Qf4,Qg5,Qh6,Qd1,Qc1,Bd3,Bc4,Bb5+,Bxa6,Bf1,Bd1,g3,g4,h3,Ra2,Ra3,Ra4,Rxa5,Rb1,Rc1,Rd1,Kf1,Kd1,Rg1,Rf1,O-O",
    "e5,b4,Na4,Nb5,Nd1,Nb1,Na2,Nd4,Ne5,Ng5,Nxh4,Ng1,Ba3,Bc1,Qd3,Qd4,Qe3,Qf4,Qg5,Qh6,Qd1,Qc1,Bd3,Bc4,Bb5+,Bxa6,Bf1,Bd1,g3,g4,h3,Ra2,Ra3,Ra4,Rxa5,Rb1,Rc1,Rd1,Kf1,Kd1,Rg1,Rf1"
]


fens = [
    "8/2k5/8/3B4/8/7b/3K4/8 b - - 0 27",
    "8/2k5/8/8/2Q5/4n2q/4K3/8 w - - 4 28",
    "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
    "rnbqkbnr/pppppp1p/6p1/8/1P6/8/P1PPPPPP/RNBQKBNR w KQkq - 0 2",
    "rn1qkbnr/ppp1pppp/8/3p4/3P2b1/5N2/PPP1PPPP/RNBQKB1R w KQkq - 2 3",
    "rn1qkbnr/ppp1ppp1/8/3p4/3P2p1/8/PPP1PPPP/RNBQKB1R w KQkq - 0 5",
    "rn1qkbnr/ppp1ppp1/8/3p4/3P2pP/8/PPP1PPP1/RNBQKB1R b KQkq h3 0 5",
    "rn1qkbnr/ppp1ppp1/8/3p4/3P4/7p/PPP1PPP1/RNBQKB1R w KQkq - 0 6",
    "rn1qkbnR/ppp1ppp1/8/3p4/2PP4/8/PP2PPp1/RNBQKB2 b Qq - 0 7",
    "r4k2/pppqpppq/8/8/1npP1B2/2N3Q1/PP2PPB1/2R1K3 b - - 1 15",
    "rnbqkbnr/p2ppppp/8/1ppP4/8/8/PPP1PPPP/RNBQKBNR w KQkq c6 0 3",
    "r1bqk2r/1P1pppbp/p1n2np1/2pP4/4P3/8/1PP2PPP/RNBQKBNR w KQkq - 1 8",
    "r2qk2r/1b1pppbp/p4np1/n1pP4/4P3/5N2/1PP1BPPP/RNBQK2R w KQkq - 2 10",
    "r3k2r/1bqpppbp/p4np1/n1pP4/4P3/1P3N2/1BP1BPPP/RN1QK2R b KQkq - 2 11",
    "r3k2r/1bq1ppb1/p2p1np1/n1pP4/4P2p/1PN2N2/1BPQBPPP/R3K2R w KQkq - 0 14",
    "r3k2r/1bq1ppb1/p2p1np1/n1pP4/4P2p/1PN2N2/1BPQBPPP/R3K2R w Kk - 4 16",
    "r3k2r/1bq1ppb1/p2p1np1/n1pP4/4P2p/1PN2N2/1BPQBPPP/R3K2R w - - 8 18",
]


def board_number_to_field(board_number):
    columns = ["h", "g", "f", "e", "d", "c", "b", "a"]
    rows = ["1", "2", "3", "4", "5", "6", "7", "8"]

    # Calculate column and row
    column = columns[board_number % 8]
    row = rows[board_number // 8]
    # Combine column and row to get the field
    field = column + row
    return field


def convert_order(algebraic, long_algebraic_notation, boardarray):

    def find_to_moves(index, from_moves, piece, From):
        to_moves = []
        if piece == "P":
            for i in algoP:
                n = i+From
                if n > -1 and n < 64:
                    a = board_number_to_field(n)
                    for index in from_moves:
                        move = long_algebraic_notation[index]
                        if a in move[2:4]:
                            to_moves.append(index)

        elif piece == "N":
            for i in algoN:
                n = i+From
                if n > -1 and n < 64:
                    a = board_number_to_field(n)
                    for index in from_moves:
                        move = long_algebraic_notation[index]
                        if a in move[2:4]:
                            to_moves.append(index)

        elif piece == "B":
            for i in algoB:
                n = i+From
                if n > -1 and n < 64:
                    a = board_number_to_field(n)
                    for index in from_moves:
                        move = long_algebraic_notation[index]
                        if a in move[2:4]:
                            to_moves.append(index)
        elif piece == "R":
            for i in algoR:
                n = i+From
                if n > -1 and n < 64:
                    a = board_number_to_field(n)
                    for index in from_moves:
                        move = long_algebraic_notation[index]
                        if a in move[2:4]:
                            to_moves.append(index)
        elif piece == "Q":
            for i in algoQ:
                n = i+From
                if n > -1 and n < 64:
                    a = board_number_to_field(n)
                    for index in from_moves:
                        move = long_algebraic_notation[index]
                        if a in move[2:4]:
                            to_moves.append(index)
        elif piece == "K":
            for i in algoK:
                n = i+From
                if n > -1 and n < 64:
                    a = board_number_to_field(n)
                    for index in from_moves:
                        move = long_algebraic_notation[index]
                        if a in move[2:4]:
                            to_moves.append(index)

        return to_moves

    def find_from_moves(move, From):

        result = []
        matching_moves_indices = [
            index for index, notation in enumerate(long_algebraic_notation) if notation[0:2] == move
        ]

        if len(matching_moves_indices) > 0:
            res = find_to_moves(From, matching_moves_indices,
                                boardarray[From], From)
            if len(res) > 0:
                result.append(res)
        return result

    my_order = []
    result = []
    for From, value in enumerate(squares):
        result = find_from_moves(value, 63-From)
        if len(result) > 0:
            my_order.append(result)
    flattened_array = [item for sublist in my_order for item in sublist[0]]

    for move in flattened_array:
        result.append(algebraic[move])

    return result


n = 0


def get_board_array(board):
    board_array = []
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        board_array.append(piece.symbol() if piece else ".")
    return board_array


for fen in fens:
    board.set_fen(fen)
    boardarray = get_board_array(board)
    algebraic = [board.san(move) for move in board.legal_moves]
    long_algebraic_notation = [str(move) for move in board.legal_moves]
    res = convert_order(algebraic, long_algebraic_notation, boardarray)
    print("-----------------")
    print(res)
    if (",".join(res) == ar[n]):
        print("OK")
    else:
        print(long_algebraic_notation)
        print(",".join(res))
        print(ar[n])
        print("-----------------")
    n += 1


# Print the board
