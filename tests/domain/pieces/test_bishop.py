from chess.domain.color import Color
from chess.domain.game_state import GameStateFactory
from chess.domain.moves.move_generator import moves_for
from chess.domain.pieces.bishop import Bishop
from chess.domain.pieces.pawn import Pawn
from chess.domain.square import Square


def test_bishop_options_from_start_position():
    game_state = GameStateFactory.create_initial_game_state()
    source = Square.from_string('c1')
    bishop = game_state.get_piece(source)
    count_moves = 0 
    for move in moves_for(game_state, source):
        count_moves += 1
    assert count_moves == 0
    assert isinstance(bishop, Bishop)
    assert bishop.color is Color.WHITE

def test_bishop_options_empty_board():
    game_state = GameStateFactory.create_empty_game_state()
    bishop = Bishop(Color.WHITE)
    source = Square.from_string('d4')
    game_state.place_piece(bishop, source, False)
    moves = set()
    moves.update([
        Square.from_string('a1'),
        Square.from_string('b2'),
        Square.from_string('c3'),
        Square.from_string('c5'),
        Square.from_string('b6'),
        Square.from_string('a7'),
        Square.from_string('e3'),
        Square.from_string('f2'),
        Square.from_string('g1'),
        Square.from_string('e5'),
        Square.from_string('f6'),
        Square.from_string('g7'),
        Square.from_string('h8'),
    ])
    count_moves = 0
    for move in moves_for(game_state, source):
        assert move in moves
        count_moves += 1
    assert count_moves == 13

def test_bishop_options_with_emenies():
    game_state = GameStateFactory.create_empty_game_state()
    bishop = Bishop(Color.WHITE)
    source = Square.from_string('d4')
    game_state.place_piece(bishop, source, False)
    game_state.place_piece(Pawn(Color.BLACK), Square.from_string('f6'), False)
    game_state.place_piece(Pawn(Color.BLACK), Square.from_string('f2'), False)
    moves = set()
    moves.update([
        Square.from_string('a1'),
        Square.from_string('b2'),
        Square.from_string('c3'),
        Square.from_string('c5'),
        Square.from_string('b6'),
        Square.from_string('a7'),
        Square.from_string('e3'),
        Square.from_string('f2'),
        Square.from_string('e5'),
        Square.from_string('f6'),
    ])

    count_moves = 0
    for move in moves_for(game_state, source):
        assert move in moves
        count_moves += 1
    assert count_moves == 10

def test_bishop_options_with_allies():
    game_state = GameStateFactory.create_empty_game_state()
    bishop = Bishop(Color.WHITE)
    source = Square.from_string('d4')
    game_state.place_piece(bishop, source, False)
    game_state.place_piece(Pawn(Color.WHITE), Square.from_string('f6'), False)
    game_state.place_piece(Pawn(Color.WHITE), Square.from_string('f2'), False)
    moves = set()
    moves.update([
        Square.from_string('a1'),
        Square.from_string('b2'),
        Square.from_string('c3'),
        Square.from_string('c5'),
        Square.from_string('b6'),
        Square.from_string('a7'),
        Square.from_string('e3'),
        Square.from_string('e5'),
    ])
    count_moves = 0
    for move in moves_for(game_state, source):
        assert move in moves
        count_moves += 1
    assert count_moves == 8