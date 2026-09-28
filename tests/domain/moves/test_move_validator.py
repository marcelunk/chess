from chess.domain.color import Color
from chess.domain.game_state import GameStateFactory
from chess.domain.moves.move_generator import squares_between
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

def test_squares_between_d4_and_a1():
    squares = list()
    for square in squares_between(Square.from_string('d4'), Square.from_string('a1')):
        squares.append(square)

    expected = [Square.from_string('c3'), Square.from_string('b2')]
    assert expected == squares

def test_squares_between_d4_and_f4():
    squares = list()
    for square in squares_between(Square.from_string('d4'), Square.from_string('f4')):
        squares.append(square)

    expected = [Square.from_string('e4')]
    assert expected == squares

def test_squares_between_d4_and_d8():
    squares = list()
    for square in squares_between(Square.from_string('d4'), Square.from_string('d8')):
        squares.append(square)

    expected = [Square.from_string('d5'), Square.from_string('d6'), Square.from_string('d7')]
    assert expected == squares

def test_squares_between_d4_and_a7():
    squares = list()
    for square in squares_between(Square.from_string('d4'), Square.from_string('a7')):
        squares.append(square)

    expected = [Square.from_string('c5'), Square.from_string('b6')]
    assert expected == squares

def test_squares_between_d4_and_e2():
    squares = list()
    for square in squares_between(Square.from_string('d4'), Square.from_string('e2')):
        squares.append(square)

    assert [] == squares

def test_squares_between_d4_and_e5():
    squares = list()
    for square in squares_between(Square.from_string('d4'), Square.from_string('e5')):
        squares.append(square)

    assert [] == squares

def test_squares_between_d4_and_c4():
    squares = list()
    for square in squares_between(Square.from_string('d4'), Square.from_string('c4')):
        squares.append(square)

    assert [] == squares