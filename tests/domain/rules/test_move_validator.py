from chess.domain.color import Color
from chess.domain.game_state import GameStateFactory
from chess.domain.pieces.queen import Queen
from chess.domain.moves.move_validator import validate_move
from chess.domain.square import Square


def test_piece_can_not_move_outside_of_board_bottom_left_corner():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square.from_string('a1')
    game_state.place_piece(Queen(Color.WHITE), source, False)
    assert not validate_move(source, Square(-1, 0), game_state, Color.WHITE)
    assert not validate_move(source, Square(-1, -1), game_state, Color.WHITE)
    assert not validate_move(source, Square(0, -1), game_state, Color.WHITE)
    assert not validate_move(source, Square(1, -1), game_state, Color.WHITE)
    assert not validate_move(source, Square(-1, 1), game_state, Color.WHITE)

def test_piece_can_not_move_outside_of_board_top_left_corner():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square.from_string('a8')
    game_state.place_piece(Queen(Color.WHITE), source, False)
    assert not validate_move(source, Square(-1, 6), game_state, Color.WHITE)
    assert not validate_move(source, Square(-1, 8), game_state, Color.WHITE)
    assert not validate_move(source, Square(0, 8), game_state, Color.WHITE)
    assert not validate_move(source, Square(1, 8), game_state, Color.WHITE)
    assert not validate_move(source, Square(2, 8), game_state, Color.WHITE)

def test_piece_can_not_move_outside_of_board_bottom_right_corner():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square.from_string('h1')
    game_state.place_piece(Queen(Color.WHITE), source, False)
    assert not validate_move(source, Square(6, -1), game_state, Color.WHITE)
    assert not validate_move(source, Square(7, -1), game_state, Color.WHITE)
    assert not validate_move(source, Square(8, -1), game_state, Color.WHITE)
    assert not validate_move(source, Square(8, 0), game_state, Color.WHITE)
    assert not validate_move(source, Square(8, 1), game_state, Color.WHITE)

def test_piece_can_not_move_outside_of_board_top_right_corner():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square.from_string('h8')
    game_state.place_piece(Queen(Color.WHITE), source, False)
    assert not validate_move(source, Square(6, 8), game_state, Color.WHITE)
    assert not validate_move(source, Square(7, 8), game_state, Color.WHITE)
    assert not validate_move(source, Square(8, 8), game_state, Color.WHITE)
    assert not validate_move(source, Square(8, 7), game_state, Color.WHITE)
    assert not validate_move(source, Square(8, 6), game_state, Color.WHITE)

def test_invalid_move_due_to_king_not_safe():
    pass