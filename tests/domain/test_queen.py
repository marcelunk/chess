from chess.domain.color import Color
from chess.domain.game_state import GameStateFactory
from chess.domain.pieces.pawn import Pawn
from chess.domain.pieces.queen import Queen
from chess.domain.rules.move_validator import _get_legal_moves
from chess.domain.square import Square


def test_queen_options_from_start_position():
    game_state = GameStateFactory.create_initial_game_state()
    source = Square.from_string('d1')
    queen = game_state.get_piece(source)
    moves = _get_legal_moves(source, game_state, queen)
    assert isinstance(queen, Queen)
    assert queen.color is Color.WHITE
    assert len(moves) == 0

def test_queen_options_empty_board():
    game_state = GameStateFactory.create_empty_game_state()
    queen = Queen(Color.WHITE)
    source = Square.from_string('d4')
    game_state.place_piece(queen, source, False)
    moves = _get_legal_moves(source, game_state, queen)
    assert len(moves) == 27
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


def test_queen_options_with_emenies():
    game_state = GameStateFactory.create_empty_game_state()
    queen = Queen(Color.WHITE)
    source = Square.from_string('d4')
    game_state.place_piece(queen, source, False)
    game_state.place_piece(Pawn(Color.BLACK), Square.from_string('b6'), False)
    game_state.place_piece(Pawn(Color.BLACK), Square.from_string('e4'), False)
    moves = _get_legal_moves(source, game_state, queen)
    assert len(moves) == 23
    assert Square.from_string('a4') in moves
    assert Square.from_string('b4') in moves
    assert Square.from_string('c4') in moves
    assert Square.from_string('e4') in moves
    assert Square.from_string('d1') in moves
    assert Square.from_string('d2') in moves
    assert Square.from_string('d3') in moves
    assert Square.from_string('d5') in moves
    assert Square.from_string('d6') in moves
    assert Square.from_string('d7') in moves
    assert Square.from_string('d8') in moves
    assert Square.from_string('a1') in moves
    assert Square.from_string('b2') in moves
    assert Square.from_string('c3') in moves
    assert Square.from_string('c5') in moves
    assert Square.from_string('b6') in moves
    assert Square.from_string('e3') in moves
    assert Square.from_string('f2') in moves
    assert Square.from_string('g1') in moves
    assert Square.from_string('e5') in moves
    assert Square.from_string('f6') in moves
    assert Square.from_string('g7') in moves
    assert Square.from_string('h8') in moves

def test_queen_options_with_allies():
    game_state = GameStateFactory.create_empty_game_state()
    queen = Queen(Color.WHITE)
    source = Square.from_string('d4')
    game_state.place_piece(queen, source, False)
    game_state.place_piece(Pawn(Color.WHITE), Square.from_string('b6'), False)
    game_state.place_piece(Pawn(Color.WHITE), Square.from_string('e4'), False)
    moves = _get_legal_moves(source, game_state, queen)
    assert len(moves) == 21
    assert Square.from_string('a4') in moves
    assert Square.from_string('b4') in moves
    assert Square.from_string('c4') in moves
    assert Square.from_string('d1') in moves
    assert Square.from_string('d2') in moves
    assert Square.from_string('d3') in moves
    assert Square.from_string('d5') in moves
    assert Square.from_string('d6') in moves
    assert Square.from_string('d7') in moves
    assert Square.from_string('d8') in moves
    assert Square.from_string('a1') in moves
    assert Square.from_string('b2') in moves
    assert Square.from_string('c3') in moves
    assert Square.from_string('c5') in moves
    assert Square.from_string('e3') in moves
    assert Square.from_string('f2') in moves
    assert Square.from_string('g1') in moves
    assert Square.from_string('e5') in moves
    assert Square.from_string('f6') in moves
    assert Square.from_string('g7') in moves
    assert Square.from_string('h8') in moves