import pytest
from chess.application.game_service import GameService
from chess.domain.color import Color
from chess.domain.square import Square


def test_invalid_input():
    game_service = GameService()
    game_service.new_game()
    with pytest.raises(RuntimeError):
        game_service.make_move("a1i3")
    with pytest.raises(RuntimeError):
        game_service.make_move("a4h9")
    with pytest.raises(RuntimeError):
        game_service.make_move("i9b0")

def test_valid_input():
    game_service = GameService()
    game_service.new_game()
    game_service.make_move("a2a3")

def test_changing_turns():
    game_service = GameService()
    game_service.new_game()

    assert game_service.turn() is Color.WHITE
    
    game_service.make_move("b2b4")
    assert game_service.turn() is Color.BLACK

    game_service.make_move("b8c6")
    assert game_service.turn() is Color.WHITE

def test_require_game():
    # TODO
    pass

def test_undo_last_move():
    # TODO
    pass

def test_redo_last_move():
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