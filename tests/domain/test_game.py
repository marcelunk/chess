import pytest
from chess.domain.color import Color
from chess.domain.game import Game


def test_invalid_input():
    game = Game()
    with pytest.raises(RuntimeError):
        game.make_move("invalid")
    with pytest.raises(RuntimeError):
        game.make_move("a1i3")
    with pytest.raises(RuntimeError):
        game.make_move("a4h9")
    with pytest.raises(RuntimeError):
        game.make_move("i9b0")
    with pytest.raises(RuntimeError):
        game.make_move("a2b-1")

def test_valid_input():
    game = Game()
    input = "a2a3"
    game.make_move(input)

def test_changing_turns():
    game = Game()
    assert game.turn is Color.WHITE
    assert len(game.history) == 0

    game.make_move('b2b4')
    assert game.turn is Color.BLACK
    assert len(game.history) == 1

    game.make_move('b8c6')
    assert game.turn is Color.WHITE
    assert len(game.history) == 2