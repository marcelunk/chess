from __future__ import annotations
from chess.domain.color import Color
from chess.domain.piece import Piece
from chess.domain.pieces.bishop import Bishop
from chess.domain.pieces.king import King
from chess.domain.pieces.knight import Knight
from chess.domain.pieces.pawn import Pawn
from chess.domain.pieces.queen import Queen
from chess.domain.pieces.rook import Rook
from chess.domain.square import Square

class GameState:

    def __init__(self, state, en_passant_square):
        self._piece_by_square = state
        self.en_passant_square = en_passant_square

    def place_piece(self, piece: Piece, square: Square):
        self._piece_by_square[square] = piece

    def get_piece(self, square: Square) -> Piece:
        return self._piece_by_square[square]

    def make_move(self, source: Square, target: Square) -> GameState:
        new_state = self._piece_by_square.copy()
        en_passant_square = None
        moving_piece = new_state[source]
        new_state[target] = moving_piece
        new_state[source] = None
        if moving_piece.in_start_position:
            moving_piece.in_start_position = False
            diff = source.rank - target.rank
            moved_two_squares = (diff) % 2 == 0
            if isinstance(moving_piece, Pawn) and moved_two_squares:
                en_passant_square = Square(source.file, source.rank + (diff/2))
        return GameState(new_state, en_passant_square)

    def __str__(self):
        squares = list(self._piece_by_square.keys())
        squares.sort()
        board = ""
        length = len(squares)
        for i in range(0, length):
            square = squares[i]
            board += str(square)
            if self._piece_by_square[square] is not None:
                board += f"({str(self._piece_by_square[square])})"
            board += ", "

            n = (i+1)
            if n % 8 == 0 and n < length:
                board += "\n"

        return board


class GameStateFactory:

    @staticmethod
    def create_empty_game_state() -> GameState:
        piece_by_square = GameStateFactory._init_empty_board()
        return GameState(piece_by_square, None)

    @staticmethod
    def create_initial_game_state() -> GameState:
        piece_by_square = GameStateFactory._init_empty_board()
        GameStateFactory._init_pieces(piece_by_square)
        return GameState(piece_by_square, None)

    @staticmethod
    def _init_empty_board():
        list_of_pairs = [(Square(file, rank), None) for file in range(8) for rank in range(8)]
        return dict(iter(list_of_pairs))

    @staticmethod
    def _init_pieces(piece_by_square):
        white_pawns = GameStateFactory._create_pieces(Pawn, 8, Color.WHITE)
        for i in range(0, 8):
            GameStateFactory._init_square(Square(i, 1), white_pawns[i], piece_by_square)
        white_rooks = GameStateFactory._create_pieces(Rook, 2, Color.WHITE)
        GameStateFactory._init_square(Square(0, 0), white_rooks[0], piece_by_square)
        GameStateFactory._init_square(Square(7, 0), white_rooks[1], piece_by_square)
        white_knights = GameStateFactory._create_pieces(Knight, 2, Color.WHITE)
        GameStateFactory._init_square(Square(1, 0), white_knights[0], piece_by_square)
        GameStateFactory._init_square(Square(6, 0), white_knights[1], piece_by_square)
        white_bishops = GameStateFactory._create_pieces(Bishop, 2, Color.WHITE)
        GameStateFactory._init_square(Square(2, 0), white_bishops[0], piece_by_square)
        GameStateFactory._init_square(Square(5, 0), white_bishops[1], piece_by_square)
        GameStateFactory._init_square(Square(3, 0), Queen(Color.WHITE), piece_by_square)
        GameStateFactory._init_square(Square(4, 0), King(Color.WHITE), piece_by_square)

        black_pawns = GameStateFactory._create_pieces(Pawn, 8, Color.BLACK)
        for i in range(0, 8):
            GameStateFactory._init_square(Square(i, 6), black_pawns[i], piece_by_square)
        black_rooks = GameStateFactory._create_pieces(Rook, 2, Color.BLACK)
        GameStateFactory._init_square(Square(0, 7), black_rooks[0], piece_by_square)
        GameStateFactory._init_square(Square(7, 7), black_rooks[1], piece_by_square)
        black_knights = GameStateFactory._create_pieces(Knight, 2, Color.BLACK)
        GameStateFactory._init_square(Square(1, 7), black_knights[0], piece_by_square)
        GameStateFactory._init_square(Square(6, 7), black_knights[1], piece_by_square)
        black_bishops = GameStateFactory._create_pieces(Bishop, 2, Color.BLACK)
        GameStateFactory._init_square(Square(2, 7), black_bishops[0], piece_by_square)
        GameStateFactory._init_square(Square(5, 7), black_bishops[1], piece_by_square)
        GameStateFactory._init_square(Square(3, 7), Queen(Color.BLACK), piece_by_square)
        GameStateFactory._init_square(Square(4, 7), King(Color.BLACK), piece_by_square)

    @staticmethod
    def _create_pieces(type, amount, color):
        pieces = list()
        count = 0
        while count < amount:
            pieces.append(type(color))
            count += 1
        return pieces 

    @staticmethod
    def _init_square(square: Square, piece: Piece, piece_by_square):
        if piece_by_square[square] is None:
            piece_by_square[square] = piece
        else:
            raise RuntimeError("Field is already initialized")