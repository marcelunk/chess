from chess.domain.color import Color
from chess.domain.game_state import GameState
from chess.domain.moves.move_generator import moves_to, squares_between
from chess.domain.pieces.rook import Rook
from chess.domain.rules.check_detector import is_in_check
from chess.domain.square import Square


def long_rochade_is_possible(game_state: GameState, turn: Color) -> bool:
    square_king = game_state.get_king_square(turn)
    if not _state_of_king_is_valid(game_state, square_king, turn):
        return False

    square_rook = None
    if turn is Color.WHITE:
        square_rook = Square(0, 0)
    else:
        square_rook = Square(0, 7)

    if not _state_of_rook_is_valid(game_state, square_rook):
        return False

    if _squares_are_blocked(game_state, square_king, square_rook):
        return False

    if _squares_are_threatend(game_state, square_king, square_rook, turn):
        return False

    return True
    
def short_rochade_is_possible(game_state: GameState, turn: Color) -> bool:
    square_king = game_state.get_king_square(turn)
    if not _state_of_king_is_valid(game_state, square_king, turn):
        return False

    square_rook = None
    if turn is Color.WHITE:
        square_rook = Square(7, 0)
    else:
        square_rook = Square(7, 7)

    if not _state_of_rook_is_valid(game_state, square_rook):
        return False

    if _squares_are_blocked(game_state, square_king, square_rook):
        return False

    if _squares_are_threatend(game_state, square_king, square_rook, turn):
        return False

    return True

def _state_of_king_is_valid(game_state, square_king, turn):
    king = game_state.get_piece(square_king)
    return king.in_start_position and not is_in_check(game_state, turn)

def _state_of_rook_is_valid(game_state, square_rook):
    piece = game_state.get_piece(square_rook)
    return isinstance(piece, Rook) and piece.in_start_position

def _squares_are_blocked(game_state, square_king, square_rook):
    return any(game_state.get_piece(square) is not None for square in squares_between(square_king, square_rook))

def _squares_are_threatend(game_state, square_king, square_rook, turn):
    for square in squares_between(square_king, square_rook):
        if any(moves_to(game_state, square, turn.opposite)):
            return True

    return False