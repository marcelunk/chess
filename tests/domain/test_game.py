import pytest
from chess.application.errors.application_errors import InvalidInputError
from chess.domain.color import Color
from chess.domain.errors.domain_errors import InvalidMoveError
from chess.domain.game import Game
from chess.domain.square import Square


def test_invalid_input():
    game = Game()
    with pytest.raises(InvalidMoveError):
        game.make_move(Square.from_string("a1"), Square.from_string("i3"))
    with pytest.raises(InvalidMoveError):
        game.make_move(Square.from_string("a4"), Square.from_string("h9"))
    with pytest.raises(InvalidMoveError):
        game.make_move(Square.from_string("i9"), Square.from_string("b0"))

def test_valid_input():
    game = Game()
    game.make_move(Square.from_string("a2"), Square.from_string("a3"))

def test_changing_turns():
    game = Game()
    assert game.turn is Color.WHITE
    assert len(game.history) == 0

    game.make_move(Square.from_string("b2"), Square.from_string("b4"))
    assert game.turn is Color.BLACK
    assert len(game.history) == 1

    game.make_move(Square.from_string("b8"), Square.from_string("c6"))
    assert game.turn is Color.WHITE
    assert len(game.history) == 2

def test_undo_last_move():
    # TODO
    pass

def test_end_game():
    # TODO
    pass

def test_white_starts():
    # TODO
    pass

def test_turns_changing():
    # TODO
    pass