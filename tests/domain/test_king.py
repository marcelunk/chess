from chess.domain.color import Color
from chess.domain.game_state import GameStateFactory
from chess.domain.pieces.pawn import Pawn
from chess.domain.pieces.king import King
from chess.domain.rules.move_validator import _get_legal_moves
from chess.domain.square import Square


def test_king_options_from_start_position():
    game_state = GameStateFactory.create_initial_game_state()
    source = Square.from_string('e1')
    king = game_state.get_piece(source)
    moves = _get_legal_moves(source, game_state, king)
    assert isinstance(king, King)
    assert king.color is Color.WHITE
    assert len(moves) == 0

def test_king_options_empty_board():
    game_state = GameStateFactory.create_empty_game_state()
    king = King(Color.WHITE)
    source = Square.from_string('d4')
    game_state.place_piece(king, source)
    moves = _get_legal_moves(source, game_state, king)
    assert len(moves) == 8
    assert Square.from_string('c4') in moves
    assert Square.from_string('e4') in moves
    assert Square.from_string('d5') in moves
    assert Square.from_string('d3') in moves
    assert Square.from_string('e5') in moves
    assert Square.from_string('e3') in moves
    assert Square.from_string('c3') in moves
    assert Square.from_string('c5') in moves


def test_king_options_with_emenies():
    game_state = GameStateFactory.create_empty_game_state()
    king = King(Color.WHITE)
    source = Square.from_string('d4')
    game_state.place_piece(king, source)
    game_state.place_piece(Pawn(Color.BLACK), Square.from_string('e5'))
    game_state.place_piece(Pawn(Color.BLACK), Square.from_string('d3'))
    moves = _get_legal_moves(source, game_state, king)
    assert len(moves) == 8
    assert Square.from_string('c4') in moves
    assert Square.from_string('e4') in moves
    assert Square.from_string('d5') in moves
    assert Square.from_string('d3') in moves
    assert Square.from_string('e5') in moves
    assert Square.from_string('e3') in moves
    assert Square.from_string('c3') in moves
    assert Square.from_string('c5') in moves

def test_king_options_with_allies():
    game_state = GameStateFactory.create_empty_game_state()
    king = King(Color.WHITE)
    source = Square.from_string('d4')
    game_state.place_piece(king, source)
    game_state.place_piece(Pawn(Color.WHITE), Square.from_string('e5'))
    game_state.place_piece(Pawn(Color.WHITE), Square.from_string('d3'))
    moves = _get_legal_moves(source, game_state, king)
    assert len(moves) == 6
    assert Square.from_string('c4') in moves
    assert Square.from_string('e4') in moves
    assert Square.from_string('d5') in moves
    assert Square.from_string('e3') in moves
    assert Square.from_string('c3') in moves
    assert Square.from_string('c5') in moves