from chess.domain.color import Color
from chess.domain.game_state import GameStateFactory
from chess.domain.moves.move_generator import moves_for
from chess.domain.pieces.pawn import Pawn
from chess.domain.pieces.king import King
from chess.domain.square import Square


def test_king_options_from_start_position():
    game_state = GameStateFactory.create_initial_game_state()
    source = Square.from_string('e1')
    king = game_state.get_piece(source)
    count_moves = 0
    for move in moves_for(game_state, source):
        count_moves += 1
    assert isinstance(king, King)
    assert king.color is Color.WHITE
    assert count_moves == 0

def test_king_options_empty_board():
    game_state = GameStateFactory.create_empty_game_state()
    king = King(Color.WHITE)
    source = Square.from_string('d4')
    game_state.place_piece(king, source, False)
    moves = set()
    moves.update([
        Square.from_string('c4'),
        Square.from_string('e4'),
        Square.from_string('d5'),
        Square.from_string('d3'),
        Square.from_string('e5'),
        Square.from_string('e3'),
        Square.from_string('c3'),
        Square.from_string('c5'),
    ])
    count_moves = 0
    for move in moves_for(game_state, source):
        assert move in moves
        count_moves += 1
    assert count_moves == 8


def test_king_options_with_emenies():
    game_state = GameStateFactory.create_empty_game_state()
    king = King(Color.WHITE)
    source = Square.from_string('d4')
    game_state.place_piece(king, source, False)
    game_state.place_piece(Pawn(Color.BLACK), Square.from_string('e5'), False)
    game_state.place_piece(Pawn(Color.BLACK), Square.from_string('d3'), False)
    moves = set()
    moves.update([
        Square.from_string('c4'),
        Square.from_string('e4'),
        Square.from_string('d5'),
        Square.from_string('d3'),
        Square.from_string('e5'),
        Square.from_string('e3'),
        Square.from_string('c3'),
        Square.from_string('c5'),
    ])
    count_moves = 0
    for move in moves_for(game_state, source):
        count_moves += 1
        assert move in moves
    assert count_moves == 8

def test_king_options_with_allies():
    game_state = GameStateFactory.create_empty_game_state()
    king = King(Color.WHITE)
    source = Square.from_string('d4')
    game_state.place_piece(king, source, False)
    game_state.place_piece(Pawn(Color.WHITE), Square.from_string('e5'), False)
    game_state.place_piece(Pawn(Color.WHITE), Square.from_string('d3'), False)
    moves = set()
    moves.update([
        Square.from_string('c4'),
        Square.from_string('e4'),
        Square.from_string('d5'),
        Square.from_string('e3'),
        Square.from_string('c3'),
        Square.from_string('c5'),
    ])
    count_moves = 0
    for move in moves_for(game_state, source):
        assert move in moves
        count_moves += 1
    assert len(moves) == 6