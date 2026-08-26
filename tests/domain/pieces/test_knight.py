from chess.domain.color import Color
from chess.domain.game_state import GameStateFactory
from chess.domain.moves.move_generator import moves_for
from chess.domain.pieces.knight import Knight
from chess.domain.pieces.pawn import Pawn
from chess.domain.moves.move_validator import _get_moves
from chess.domain.square import Square


def test_knight_options_from_start_position():
    game_state = GameStateFactory.create_initial_game_state()
    source = Square.from_string('b1')
    knight = game_state.get_piece(source)
    moves = set()
    moves.update([
        Square.from_string('a3'),
        Square.from_string('c3'),
    ])
    count_moves = 0
    for move in moves_for(game_state, source):
        assert move in moves
        count_moves += 1
    assert isinstance(knight, Knight)
    assert knight.color is Color.WHITE
    assert count_moves == 2

def test_knight_options_empty_board():
    game_state = GameStateFactory.create_empty_game_state()
    knight = Knight(Color.WHITE)
    source = Square.from_string('d4')
    game_state.place_piece(knight, source, False)
    moves = set()
    moves.update([
        Square.from_string('b3'),
        Square.from_string('c2'),
        Square.from_string('e2'),
        Square.from_string('f3'),
        Square.from_string('e6'),
        Square.from_string('f5'),
        Square.from_string('b5'),
        Square.from_string('c6'),
    ])
    count_moves = 0
    for move in moves_for(game_state, source):
        assert move in moves
        count_moves += 1
    assert count_moves == 8

def test_knight_options_with_emenies():
    game_state = GameStateFactory.create_empty_game_state()
    knight = Knight(Color.WHITE)
    source = Square.from_string('b4')
    game_state.place_piece(knight, source, False)
    game_state.place_piece(Pawn(Color.BLACK), Square.from_string('c6'), False)
    game_state.place_piece(Pawn(Color.BLACK), Square.from_string('a2'), False)
    moves = set()
    moves.update([
        Square.from_string('c6'),
        Square.from_string('a2'),
        Square.from_string('a6'),
        Square.from_string('d5'),
        Square.from_string('c2'),
        Square.from_string('d3'),
    ])
    count_moves = 0
    for move in moves_for(game_state, source):
        assert move in moves
        count_moves += 1
    assert count_moves == 6

def test_knight_options_with_allies():
    game_state = GameStateFactory.create_empty_game_state()
    knight = Knight(Color.WHITE)
    source = Square.from_string('b4')
    game_state.place_piece(knight, source, False)
    game_state.place_piece(Pawn(Color.WHITE), Square.from_string('c6'), False)
    game_state.place_piece(Pawn(Color.WHITE), Square.from_string('a2'), False)
    moves = set()
    moves.update([
        Square.from_string('a6'),
        Square.from_string('d5'),
        Square.from_string('c2'),
        Square.from_string('d3'),
    ])
    count_moves = 0
    for move in moves_for(game_state, source):
        assert move in moves
        count_moves += 1
    assert count_moves == 4