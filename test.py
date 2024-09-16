import chess


def order_legal_moves(board):
    # Get all legal moves
    legal_moves = list(board.legal_moves)

    # Example: Order moves by piece type (pawn, knight, bishop, rook, queen, king)
    def move_priority(move):
        piece = board.piece_at(move.from_square)
        return piece.piece_type if piece else 0

    # Sort moves based on the priority function
    ordered_moves = sorted(legal_moves, key=move_priority)

    return ordered_moves


# Create a new board
board = chess.Board()

# Get and print ordered legal moves
ordered_moves = order_legal_moves(board)
for move in ordered_moves:
    print(board.san(move))
