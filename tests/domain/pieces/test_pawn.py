from chess.domain.color import Color
from chess.domain.game_state import GameStateFactory
from chess.domain.moves.move_generator import moves_for
from chess.domain.moves.move_validator import validate_move
from chess.domain.pieces.king import King
from chess.domain.pieces.pawn import Pawn
from chess.domain.pieces.rook import Rook
from chess.domain.square import Square


def test_possible_moves_white_from_start_position():
    game_state = GameStateFactory.create_initial_game_state()
    source = Square.from_string('b2')
    moves = set()
    moves.update([
        Square.from_string('b3'),
        Square.from_string('b4'),
    ])
    count_moves = 0
    for move in moves_for(game_state, source):
        assert move in moves
        count_moves += 1
    assert count_moves == 2

def test_possible_moves_black_from_start_position():
    game_state = GameStateFactory.create_initial_game_state()
    source = Square.from_string('b7')
    moves = set()
    moves.update([
        Square.from_string('b6'),
        Square.from_string('b5'),
    ])
    count_moves = 0
    for move in moves_for(game_state, source):
        assert move in moves
        count_moves += 1
    assert count_moves == 2

def test_possible_hits_white_from_start_position():
    game_state = GameStateFactory.create_empty_game_state()
    pawn = Pawn(Color.WHITE)
    position_pawn = 'c2'
    source = Square.from_string(position_pawn)
    game_state.place_piece(pawn, source, True)
    game_state.place_piece(Rook(Color.BLACK), Square.from_string('b3'), False)
    moves = set()
    moves.update([
        Square.from_string('b3'),
        Square.from_string('c3'),
        Square.from_string('c4'),
    ])
    count_moves = 0
    for move in moves_for(game_state, source):
        assert move in moves
        count_moves += 1
    assert count_moves == 3

def test_possible_hits_black_from_start_position():
    game_state = GameStateFactory.create_empty_game_state()
    pawn = Pawn(Color.BLACK)
    position_pawn = 'c7'
    source = Square.from_string(position_pawn)
    game_state.place_piece(pawn, source, True)
    game_state.place_piece(Rook(Color.WHITE), Square.from_string('b6'), False)
    moves = set()
    moves.update([
        Square.from_string('b6'),
        Square.from_string('c6'),
        Square.from_string('c5'),
    ])
    count_moves = 0
    for move in moves_for(game_state, source):
        assert move in moves
        count_moves += 1
    assert count_moves == 3

def test_possible_hits_white():
    game_state = GameStateFactory.create_empty_game_state()
    pawn = Pawn(Color.WHITE)
    source = Square.from_string('d4')
    game_state.place_piece(pawn, source, False)
    game_state.place_piece(Rook(Color.BLACK), Square.from_string('c5'), False)
    moves = set()
    moves.update([
        Square.from_string('d5'),
        Square.from_string('c5'),
    ])
    count_moves = 0
    for move in moves_for(game_state, source):
        assert move in moves
        count_moves += 1
    assert count_moves == 2

def test_possible_hits_black():
    game_state = GameStateFactory.create_empty_game_state()
    pawn = Pawn(Color.BLACK)
    source = Square.from_string('d4')
    game_state.place_piece(pawn, source, False)
    game_state.place_piece(Rook(Color.WHITE), Square.from_string('c3'), False)
    moves = set()
    moves.update([
        Square.from_string('d3'),
        Square.from_string('c3'),
    ])
    count_moves = 0
    for move in moves_for(game_state, source):
        assert move in moves
        count_moves += 1
    assert count_moves == 2

def test_en_passant_white_pawn():
    game_state = GameStateFactory.create_empty_game_state()
    white_pawn = Pawn(Color.WHITE)
    black_pawn = Pawn(Color.BLACK)
    source_white_pawn = Square.from_string('c5')
    game_state.place_piece(white_pawn, source_white_pawn, False)
    game_state.place_piece(black_pawn, Square.from_string('b7'), True)
    game_state.place_piece(King(Color.WHITE), Square.from_string('e1'), True)
    game_state.place_piece(King(Color.BLACK), Square.from_string('e8'), True)
    next_game_state = game_state.make_move(Square.from_string('b7'), Square.from_string('b5'))
    moves = set()
    moves.update([
        Square.from_string('c6'),
    ])
    count_moves = 0
    for move in moves_for(next_game_state, source_white_pawn):
        assert move in moves
        count_moves += 1
    assert count_moves == 1
    assert validate_move(source_white_pawn, Square.from_string('b6'), next_game_state, Color.WHITE)

def test_en_passant_black_pawn():
    game_state = GameStateFactory.create_empty_game_state()
    white_pawn = Pawn(Color.WHITE)
    black_pawn = Pawn(Color.BLACK)
    game_state.place_piece(white_pawn, Square.from_string('c2'), True)
    source_black_pawn = Square.from_string('b4')
    game_state.place_piece(black_pawn, source_black_pawn, False)
    game_state.place_piece(King(Color.WHITE), Square.from_string('e1'), True)
    game_state.place_piece(King(Color.BLACK), Square.from_string('e8'), True)
    next_game_state = game_state.make_move(Square.from_string('c2'), Square.from_string('c4'))
    moves = set()
    moves.update([
        Square.from_string('b3'),
    ])
    count_moves = 0
    for move in moves_for(next_game_state, source_black_pawn):
        assert move in moves
        count_moves += 1
    assert count_moves == 1
    assert validate_move(source_black_pawn, Square.from_string('c3'), next_game_state, Color.BLACK)

def test_swap():
    pass