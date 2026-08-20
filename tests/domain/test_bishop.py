from chess.domain.color import Color
from chess.domain.game_state import GameStateFactory
from chess.domain.pieces.bishop import Bishop
from chess.domain.pieces.pawn import Pawn
from chess.domain.rules.move_validator import _get_legal_moves
from chess.domain.square import Square


def test_bishop_options_from_start_position():
    game_state = GameStateFactory.create_initial_game_state()
    source = Square.from_string('c1')
    bishop = game_state.get_piece(source)
    moves = _get_legal_moves(source, game_state, bishop)
    assert isinstance(bishop, Bishop)
    assert bishop.color is Color.WHITE
    assert len(moves) == 0

def test_bishop_options_empty_board():
    game_state = GameStateFactory.create_empty_game_state()
    bishop = Bishop(Color.WHITE)
    source = Square.from_string('d4')
    game_state.place_piece(bishop, source, False)
    moves = _get_legal_moves(source, game_state, bishop)
    assert len(moves) == 13
    assert Square.from_string('a1') in moves
    assert Square.from_string('b2') in moves
    assert Square.from_string('c3') in moves
    assert Square.from_string('c5') in moves
    assert Square.from_string('b6') in moves
    assert Square.from_string('a7') in moves
    assert Square.from_string('e3') in moves
    assert Square.from_string('f2') in moves
    assert Square.from_string('g1') in moves
    assert Square.from_string('e5') in moves
    assert Square.from_string('f6') in moves
    assert Square.from_string('g7') in moves
    assert Square.from_string('h8') in moves

def test_bishop_options_with_emenies():
    game_state = GameStateFactory.create_empty_game_state()
    bishop = Bishop(Color.WHITE)
    source = Square.from_string('d4')
    game_state.place_piece(bishop, source, False)
    game_state.place_piece(Pawn(Color.BLACK), Square.from_string('f6'), False)
    game_state.place_piece(Pawn(Color.BLACK), Square.from_string('f2'), False)
    moves = _get_legal_moves(source, game_state, bishop)
    assert len(moves) == 10
    assert Square.from_string('a1') in moves
    assert Square.from_string('b2') in moves
    assert Square.from_string('c3') in moves
    assert Square.from_string('c5') in moves
    assert Square.from_string('b6') in moves
    assert Square.from_string('a7') in moves
    assert Square.from_string('e3') in moves
    assert Square.from_string('f2') in moves
    assert Square.from_string('e5') in moves
    assert Square.from_string('f6') in moves

def test_bishop_options_with_allies():
    game_state = GameStateFactory.create_empty_game_state()
    bishop = Bishop(Color.WHITE)
    source = Square.from_string('d4')
    game_state.place_piece(bishop, source, False)
    game_state.place_piece(Pawn(Color.WHITE), Square.from_string('f6'), False)
    game_state.place_piece(Pawn(Color.WHITE), Square.from_string('f2'), False)
    moves = _get_legal_moves(source, game_state, bishop)
    assert len(moves) == 8
    assert Square.from_string('a1') in moves
    assert Square.from_string('b2') in moves
    assert Square.from_string('c3') in moves
    assert Square.from_string('c5') in moves
    assert Square.from_string('b6') in moves
    assert Square.from_string('a7') in moves
    assert Square.from_string('e3') in moves
    assert Square.from_string('e5') in moves