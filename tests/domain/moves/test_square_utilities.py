from chess.domain.moves.square_utilities import squares_between
from chess.domain.square import Square


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