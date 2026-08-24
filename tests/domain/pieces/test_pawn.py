from chess.domain.color import Color
from chess.domain.game_state import GameStateFactory
from chess.domain.pieces.pawn import Pawn
from chess.domain.pieces.rook import Rook
from chess.domain.rules.move_validator import _get_moves_pawn
from chess.domain.square import Square


def test_possible_moves_white_from_start_position():
    game_state = GameStateFactory.create_initial_game_state()
    source = Square.from_string('b2')
    pawn = game_state.get_piece(source)
    moves = _get_moves_pawn(source, game_state, pawn)
    assert len(moves) == 2
    assert Square.from_string('b3') in moves
    assert Square.from_string('b4') in moves

def test_possible_moves_black_from_start_position():
    game_state = GameStateFactory.create_initial_game_state()
    source = Square.from_string('b7')
    pawn = game_state.get_piece(source)
    moves = _get_moves_pawn(source, game_state, pawn)
    assert len(moves) == 2
    assert Square.from_string('b6') in moves
    assert Square.from_string('b5') in moves

def test_possible_hits_white_from_start_position():
    game_state = GameStateFactory.create_empty_game_state()
    pawn = Pawn(Color.WHITE)
    position_pawn = 'c2'
    game_state.place_piece(pawn, Square.from_string(position_pawn), True)
    game_state.place_piece(Rook(Color.BLACK), Square.from_string('b3'), False)
    moves = _get_moves_pawn(Square.from_string(position_pawn), game_state, pawn)
    assert len(moves) == 3
    assert Square.from_string('b3') in moves
    assert Square.from_string('c3') in moves
    assert Square.from_string('c4') in moves

def test_possible_hits_black_from_start_position():
    game_state = GameStateFactory.create_empty_game_state()
    pawn = Pawn(Color.BLACK)
    position_pawn = 'c7'
    game_state.place_piece(pawn, Square.from_string(position_pawn), True)
    game_state.place_piece(Rook(Color.WHITE), Square.from_string('b6'), False)
    moves = _get_moves_pawn(Square.from_string(position_pawn), game_state, pawn)
    assert len(moves) == 3
    assert Square.from_string('b6') in moves
    assert Square.from_string('c6') in moves
    assert Square.from_string('c5') in moves

def test_possible_hits_white():
    game_state = GameStateFactory.create_empty_game_state()
    pawn = Pawn(Color.WHITE)
    game_state.place_piece(pawn, Square.from_string('d4'), False)
    game_state.place_piece(Rook(Color.BLACK), Square.from_string('c5'), False)
    moves = _get_moves_pawn(Square.from_string('d4'), game_state, pawn)
    assert len(moves) == 2
    assert Square.from_string('d5') in moves
    assert Square.from_string('c5') in moves

def test_possible_hits_black():
    game_state = GameStateFactory.create_empty_game_state()
    pawn = Pawn(Color.BLACK)
    game_state.place_piece(pawn, Square.from_string('d4'), False)
    game_state.place_piece(Rook(Color.WHITE), Square.from_string('c3'), False)
    moves = _get_moves_pawn(Square.from_string('d4'), game_state, pawn)
    assert len(moves) == 2
    assert Square.from_string('d3') in moves
    assert Square.from_string('c3') in moves

def test_en_passant_white_pawn():
    game_state = GameStateFactory.create_empty_game_state()
    white_pawn = Pawn(Color.WHITE)
    black_pawn = Pawn(Color.BLACK)
    game_state.place_piece(white_pawn, Square.from_string('c5'), False)
    game_state.place_piece(black_pawn, Square.from_string('b7'), True)
    next_game_state = game_state.make_move(Square.from_string('b7'), Square.from_string('b5'))
    moves = _get_moves_pawn(Square.from_string('c5'), next_game_state, white_pawn)
    assert len(moves) == 2
    assert Square.from_string('b6') in moves
    assert Square.from_string('c6') in moves

def test_en_passant_black_pawn():
    game_state = GameStateFactory.create_empty_game_state()
    white_pawn = Pawn(Color.WHITE)
    black_pawn = Pawn(Color.BLACK)
    game_state.place_piece(white_pawn, Square.from_string('c2'), True)
    game_state.place_piece(black_pawn, Square.from_string('b4'), False)
    next_game_state = game_state.make_move(Square.from_string('c2'), Square.from_string('c4'))
    moves = _get_moves_pawn(Square.from_string('b4'), next_game_state, black_pawn)
    assert len(moves) == 2
    assert Square.from_string('b3') in moves
    assert Square.from_string('c3') in moves

def test_swap():
    pass