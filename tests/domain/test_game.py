import pytest
from chess.domain.game import Game
from chess.domain.pieces.pawn import Pawn


def test_invalid_input():
    game = Game()
    input = "invalid"
    with pytest.raises(RuntimeError):
        game.make_move(input)

def test_valid_input():
    game = Game()
    input = "a2a3"
    game.make_move(input)