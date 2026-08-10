from chess.domain.color import Color
from chess.domain.game_state import GameStateFactory
from chess.domain.pieces.bishop import Bishop
from chess.domain.pieces.king import King
from chess.domain.pieces.knight import Knight
from chess.domain.pieces.pawn import Pawn
from chess.domain.pieces.queen import Queen
from chess.domain.pieces.rook import Rook
from chess.domain.square import Square


def test_empty_game_state_is_empty():
    game_state = GameStateFactory.create_empty_game_state()
    for p in game_state._piece_by_square.values():
        assert p is None
    _test_color_of_squares(game_state)

def _test_color_of_squares(game_state):
    squares = list(game_state._piece_by_square.keys())
    for f in range(8):
        for r in range(8):
            i = squares.index(Square(f, r))
            if (f + r) % 2 == 0:
                assert squares[i].is_dark
            else:
                assert squares[i].is_light
    

def test_new_game_state_is_valid():
    game_state = GameStateFactory.create_initial_game_state()
    _test_white_pieces(game_state)
    _test_white_pawns(game_state)
    _test_black_pieces(game_state)
    _test_black_pawns(game_state)
    _test_empty_squares(game_state)

def _test_white_pieces(game_state):
    white_rook_one = game_state.get_piece(Square(0,0))
    assert isinstance(white_rook_one, Rook)
    assert white_rook_one.color is Color.WHITE

    white_knight_one = game_state.get_piece(Square(1,0))
    assert isinstance(white_knight_one, Knight)
    assert white_rook_one.color is Color.WHITE

    white_bishop_one = game_state.get_piece(Square(2,0))
    assert isinstance(white_bishop_one, Bishop)
    assert white_bishop_one.color is Color.WHITE

    white_queen = game_state.get_piece(Square(3,0))
    assert isinstance(white_queen, Queen)
    assert white_queen.color is Color.WHITE

    white_king = game_state.get_piece(Square(4,0))
    assert isinstance(white_king, King)
    assert white_king.color is Color.WHITE

    white_rook_two = game_state.get_piece(Square(7,0))
    assert isinstance(white_rook_two, Rook)
    assert white_rook_two.color is Color.WHITE
    assert white_rook_one is not white_rook_two

    white_knight_two = game_state.get_piece(Square(6,0))
    assert isinstance(white_knight_two, Knight)
    assert white_knight_two.color is Color.WHITE
    assert white_knight_one is not white_knight_two

    white_bishop_two = game_state.get_piece(Square(5,0))
    assert isinstance(white_bishop_two, Bishop)
    assert white_bishop_two.color is Color.WHITE
    assert white_bishop_one is not white_bishop_two


def _test_black_pieces(game_state):
    black_rook_one = game_state.get_piece(Square(0,7))
    assert isinstance(black_rook_one, Rook)
    assert black_rook_one.color is Color.BLACK

    black_knight_one = game_state.get_piece(Square(1,7))
    assert isinstance(black_knight_one, Knight)
    assert black_rook_one.color is Color.BLACK

    black_bishop_one = game_state.get_piece(Square(2,7))
    assert isinstance(black_bishop_one, Bishop)
    assert black_bishop_one.color is Color.BLACK

    black_queen = game_state.get_piece(Square(3,7))
    assert isinstance(black_queen, Queen)
    assert black_queen.color is Color.BLACK

    black_king = game_state.get_piece(Square(4,7))
    assert isinstance(black_king, King)
    assert black_king.color is Color.BLACK

    black_rook_two = game_state.get_piece(Square(7,7))
    assert isinstance(black_rook_two, Rook)
    assert black_rook_two.color is Color.BLACK
    assert black_rook_one is not black_rook_two

    black_knight_two = game_state.get_piece(Square(6,7))
    assert isinstance(black_knight_two, Knight)
    assert black_knight_two.color is Color.BLACK
    assert black_knight_one is not black_knight_two

    black_bishop_two = game_state.get_piece(Square(5,7))
    assert isinstance(black_bishop_two, Bishop)
    assert black_bishop_two.color is Color.BLACK
    assert black_bishop_one is not black_bishop_two

def _test_white_pawns(game_state):
    pawns = set()
    for i in range(8):
        pawns.add(game_state.get_piece(Square(i, 1)))

    for p in pawns:
        assert isinstance(p, Pawn)
        assert p.color is Color.WHITE

    assert len(pawns) == 8

def _test_black_pawns(game_state):
    pawns = set()
    for i in range(8):
        pawns.add(game_state.get_piece(Square(i, 6)))

    for p in pawns:
        assert isinstance(p, Pawn)
        assert p.color is Color.BLACK

    assert len(pawns) == 8

def _test_empty_squares(game_state):
    empty = 0
    occupied = 0
    for f in range(8):
        for r in range(8):
            piece = game_state.get_piece(Square(f, r))
            if piece is None:
                empty += 1
            else:
                occupied += 1
    assert empty == 32
    assert occupied == 32