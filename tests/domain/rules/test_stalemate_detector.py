from chess.domain.color import Color
from chess.domain.game_state import GameStateFactory
from chess.domain.pieces.king import King
from chess.domain.pieces.queen import Queen
from chess.domain.rules.stalemate_detector import is_stalemate
from chess.domain.square import Square


def test_white_king_in_stalemate():
    game_state = GameStateFactory.create_empty_game_state()
    game_state.place_piece(King(Color.WHITE), Square.from_string('a8'), False)
    game_state.place_piece(Queen(Color.BLACK), Square.from_string('b6'), False)
    assert is_stalemate(game_state, Color.WHITE)

def test_white_king_in_not_in_stalemate():
    game_state = GameStateFactory.create_empty_game_state()
    game_state.place_piece(King(Color.WHITE), Square.from_string('a8'), False)
    game_state.place_piece(Queen(Color.BLACK), Square.from_string('b5'), False)
    assert not is_stalemate(game_state, Color.WHITE)

def test_black_king_in_stalemate():
    game_state = GameStateFactory.create_empty_game_state()
    game_state.place_piece(King(Color.BLACK), Square.from_string('a8'), False)
    game_state.place_piece(Queen(Color.WHITE), Square.from_string('b6'), False)
    assert is_stalemate(game_state, Color.BLACK)

def test_black_king_in_not_in_stalemate():
    game_state = GameStateFactory.create_empty_game_state()
    game_state.place_piece(King(Color.BLACK), Square.from_string('a8'), False)
    game_state.place_piece(Queen(Color.WHITE), Square.from_string('b5'), False)
    assert not is_stalemate(game_state, Color.BLACK)