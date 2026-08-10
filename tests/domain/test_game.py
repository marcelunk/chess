import pytest
from chess.domain.game import Game
from chess.domain.pieces.pawn import Pawn


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

def test_valid_input():
    game = Game()
    input = "a2a3"
    game.make_move(input)