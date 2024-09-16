import chess
import chess.engine

# Path to the Stockfish executable
# Update this path
stockfish_path = "D:/program/stockfish/stockfish-windows-x86-64-avx2.exe"

# Create a new chess board
board = chess.Board()

# Initialize the Stockfish engine
with chess.engine.SimpleEngine.popen_uci(stockfish_path) as engine:
    # Evaluate the position
    info = engine.analyse(board, chess.engine.Limit(time=2.0))
    print("Score:", info["score"])
