from chess.domain.color import Color
from chess.domain.game_state import GameStateFactory
from chess.domain.moves.move_generator import moves_for
from chess.domain.pieces.pawn import Pawn
from chess.domain.pieces.rook import Rook
from chess.domain.square import Square


def test_rook_options_from_start_position():
    game_state = GameStateFactory.create_initial_game_state()
    source = Square.from_string('a1')
    rook = game_state.get_piece(source)
    assert isinstance(rook, Rook)
    assert rook.color is Color.WHITE
    moves = set()
    moves.update([
    ])
    count_moves = 0
    for move in moves_for(game_state, source):
        count_moves += 1
    assert count_moves == 0

def test_rook_options_empty_board():
    game_state = GameStateFactory.create_empty_game_state()
    rook = Rook(Color.WHITE)
    source = Square.from_string('d4')
    game_state.place_piece(rook, source, False)
    moves = set()
    moves.update([
        Square.from_string('a4'),
        Square.from_string('b4'),
        Square.from_string('c4'),
        Square.from_string('e4'),
        Square.from_string('f4'),
        Square.from_string('g4'),
        Square.from_string('h4'),
        Square.from_string('d1'),
        Square.from_string('d2'),
        Square.from_string('d3'),
        Square.from_string('d5'),
        Square.from_string('d6'),
        Square.from_string('d7'),
        Square.from_string('d8'),
    ])
    count_moves = 0
    for move in moves_for(game_state, source):
        assert move in moves
        count_moves += 1
    assert count_moves == 14

def test_rook_options_with_emenies():
    game_state = GameStateFactory.create_empty_game_state()
    rook = Rook(Color.WHITE)
    source = Square.from_string('d4')
    game_state.place_piece(rook, source, False)
    game_state.place_piece(Pawn(Color.BLACK), Square.from_string('d7'), False)
    game_state.place_piece(Pawn(Color.BLACK), Square.from_string('d3'), False)
    moves = set()
    moves.update([
        Square.from_string('a4'),
        Square.from_string('b4'),
        Square.from_string('c4'),
        Square.from_string('e4'),
        Square.from_string('f4'),
        Square.from_string('g4'),
        Square.from_string('h4'),
        Square.from_string('d3'),
        Square.from_string('d5'),
        Square.from_string('d6'),
        Square.from_string('d7'),
    ])
    count_moves = 0
    for move in moves_for(game_state, source):
        assert move in moves
        count_moves += 1
    assert count_moves == 11

def test_rook_options_with_allies():
    game_state = GameStateFactory.create_empty_game_state()
    rook = Rook(Color.WHITE)
    source = Square.from_string('d4')
    game_state.place_piece(rook, source, False)
    game_state.place_piece(Pawn(Color.WHITE), Square.from_string('d7'), False)
    game_state.place_piece(Pawn(Color.WHITE), Square.from_string('d3'), False)
    moves = set()
    moves.update([
        Square.from_string('a4'),
        Square.from_string('b4'),
        Square.from_string('c4'),
        Square.from_string('e4'),
        Square.from_string('f4'),
        Square.from_string('g4'),
        Square.from_string('h4'),
        Square.from_string('d5'),
        Square.from_string('d6'),
    ])
    count_moves = 0
    for move in moves_for(game_state, source):
        assert move in moves
        count_moves += 1
    assert count_moves == 9