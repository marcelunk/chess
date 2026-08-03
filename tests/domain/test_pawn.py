from chess.domain.game_state import GameStateFactory
from chess.domain.rules.move_validator import MoveValidator
from chess.domain.square import Square


def test_possible_moves_from_start_position():
    game_state = GameStateFactory.create_initial_game_state()
    source = Square(1, 1)
    pawn = game_state.get_piece(source)
    moves = MoveValidator._get_legal_moves(source, game_state, pawn)
    assert len(moves) == 2
    assert Square(1, 2) in moves
    assert Square(1, 3) in moves

def test_en_passant():
    pass

def test_possible_hits():
    pass

def test_swap():
    pass