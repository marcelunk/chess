from chess.domain.color import Color
from chess.domain.game_state import GameStateFactory
from chess.domain.pieces.pawn import Pawn
from chess.domain.pieces.rook import Rook
from chess.domain.rules.move_validator import _get_pawn_legal_moves
from chess.domain.square import Square


def test_possible_moves_white_from_start_position():
    game_state = GameStateFactory.create_initial_game_state()
    source = Square.from_string('b2')
    pawn = game_state.get_piece(source)
    moves = _get_pawn_legal_moves(source, game_state, pawn)
    assert len(moves) == 2
    assert Square.from_string('b3') in moves
    assert Square.from_string('b4') in moves

def test_possible_moves_black_from_start_position():
    game_state = GameStateFactory.create_initial_game_state()
    source = Square.from_string('b7')
    pawn = game_state.get_piece(source)
    moves = _get_pawn_legal_moves(source, game_state, pawn)
    assert len(moves) == 2
    assert Square.from_string('b6') in moves
    assert Square.from_string('b5') in moves

def test_en_passant():
    pass

def test_possible_hits_white():
    game_state = GameStateFactory.create_empty_game_state()
    pawn = Pawn(Color.WHITE)
    game_state.place_piece(pawn, Square.from_string('d4'), False)
    game_state.place_piece(Rook(Color.BLACK), Square.from_string('c5'), False)
    moves = _get_pawn_legal_moves(Square.from_string('d4'), game_state, pawn)
    assert len(moves) == 2
    assert Square.from_string('d5') in moves
    assert Square.from_string('c5') in moves

def test_possible_hits_black():
    pass

def test_swap():
    pass