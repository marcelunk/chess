from chess.domain.color import Color
from chess.domain.game_state import GameStateFactory
from chess.domain.pieces.pawn import Pawn
from chess.domain.pieces.rook import Rook
from chess.domain.rules.move_validator import _get_legal_moves
from chess.domain.square import Square


def test_rook_options_from_start_position():
    game_state = GameStateFactory.create_initial_game_state()
    source = Square.from_string('a1')
    rook = game_state.get_piece(source)
    assert isinstance(rook, Rook)
    assert rook.color is Color.WHITE
    moves = _get_legal_moves(source, game_state, rook)
    assert len(moves) == 0

def test_rook_options_empty_board():
    game_state = GameStateFactory.create_empty_game_state()
    rook = Rook(Color.WHITE)
    source = Square.from_string('d4')
    game_state.place_piece(rook, source)
    moves = _get_legal_moves(source, game_state, rook)
    assert len(moves) == 14
    assert Square.from_string('a4') in moves
    assert Square.from_string('b4') in moves
    assert Square.from_string('c4') in moves
    assert Square.from_string('e4') in moves
    assert Square.from_string('f4') in moves
    assert Square.from_string('g4') in moves
    assert Square.from_string('h4') in moves
    assert Square.from_string('d1') in moves
    assert Square.from_string('d2') in moves
    assert Square.from_string('d3') in moves
    assert Square.from_string('d5') in moves
    assert Square.from_string('d6') in moves
    assert Square.from_string('d7') in moves
    assert Square.from_string('d8') in moves

def test_rook_options_with_emenies():
    game_state = GameStateFactory.create_empty_game_state()
    rook = Rook(Color.WHITE)
    source = Square.from_string('d4')
    game_state.place_piece(rook, source)
    game_state.place_piece(Pawn(Color.BLACK), Square.from_string('d7'))
    game_state.place_piece(Pawn(Color.BLACK), Square.from_string('d3'))
    moves = _get_legal_moves(source, game_state, rook)
    assert len(moves) == 11
    assert Square.from_string('a4') in moves
    assert Square.from_string('b4') in moves
    assert Square.from_string('c4') in moves
    assert Square.from_string('e4') in moves
    assert Square.from_string('f4') in moves
    assert Square.from_string('g4') in moves
    assert Square.from_string('h4') in moves
    assert Square.from_string('d3') in moves
    assert Square.from_string('d5') in moves
    assert Square.from_string('d6') in moves
    assert Square.from_string('d7') in moves

def test_rook_options_with_allies():
    game_state = GameStateFactory.create_empty_game_state()
    rook = Rook(Color.WHITE)
    source = Square.from_string('d4')
    game_state.place_piece(rook, source)
    game_state.place_piece(Pawn(Color.WHITE), Square.from_string('d7'))
    game_state.place_piece(Pawn(Color.WHITE), Square.from_string('d3'))
    moves = _get_legal_moves(source, game_state, rook)
    assert len(moves) == 9
    assert Square.from_string('a4') in moves
    assert Square.from_string('b4') in moves
    assert Square.from_string('c4') in moves
    assert Square.from_string('e4') in moves
    assert Square.from_string('f4') in moves
    assert Square.from_string('g4') in moves
    assert Square.from_string('h4') in moves
    assert Square.from_string('d5') in moves
    assert Square.from_string('d6') in moves