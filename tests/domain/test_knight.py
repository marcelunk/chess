from chess.domain.color import Color
from chess.domain.game_state import GameStateFactory
from chess.domain.pieces.knight import Knight
from chess.domain.pieces.pawn import Pawn
from chess.domain.rules.move_validator import MoveValidator
from chess.domain.square import Square


def test_knight_options_from_start_position():
    game_state = GameStateFactory.create_initial_game_state()
    source = Square(1, 0)
    knight = game_state.get_piece(source)
    moves = MoveValidator._get_legal_moves(source, game_state, knight)
    assert isinstance(knight, Knight)
    assert knight.color is Color.WHITE
    assert len(moves) == 2
    assert Square.from_string('a3') in moves
    assert Square.from_string('c3') in moves

def test_knight_options_empty_board():
    game_state = GameStateFactory.create_empty_game_state()
    knight = Knight(Color.WHITE)
    source = Square(3, 3)
    game_state.place_piece(knight, source)
    moves = MoveValidator._get_legal_moves(source, game_state, knight)
    assert len(moves) == 8
    assert Square.from_string('b3') in moves
    assert Square.from_string('c2') in moves
    assert Square.from_string('e2') in moves
    assert Square.from_string('f3') in moves
    assert Square.from_string('e6') in moves
    assert Square.from_string('f5') in moves
    assert Square.from_string('b5') in moves
    assert Square.from_string('c6') in moves

def test_knight_options_with_emenies():
    game_state = GameStateFactory.create_empty_game_state()
    knight = Knight(Color.WHITE)
    source = Square.from_string('b4')
    game_state.place_piece(knight, source)
    game_state.place_piece(Pawn(Color.BLACK), Square.from_string('c6'))
    game_state.place_piece(Pawn(Color.BLACK), Square.from_string('a2'))
    moves = MoveValidator._get_legal_moves(source, game_state, knight)
    assert len(moves) == 6
    assert Square.from_string('c6') in moves
    assert Square.from_string('a2') in moves
    assert Square.from_string('a6') in moves
    assert Square.from_string('d5') in moves
    assert Square.from_string('c2') in moves
    assert Square.from_string('d3') in moves

def test_knight_options_with_allies():
    game_state = GameStateFactory.create_empty_game_state()
    knight = Knight(Color.WHITE)
    source = Square.from_string('b4')
    game_state.place_piece(knight, source)
    game_state.place_piece(Pawn(Color.WHITE), Square.from_string('c6'))
    game_state.place_piece(Pawn(Color.WHITE), Square.from_string('a2'))
    moves = MoveValidator._get_legal_moves(source, game_state, knight)
    assert len(moves) == 4
    assert Square.from_string('a6') in moves
    assert Square.from_string('d5') in moves
    assert Square.from_string('c2') in moves
    assert Square.from_string('d3') in moves