from chess.domain.color import Color
from chess.domain.game_state import GameState
from chess.domain.moves.move_generator import moves_from, moves_to


def is_stalemate(game_state: GameState, turn: Color) -> bool:
    square_king = game_state.get_king_square(turn)
    for move in moves_from(game_state, square_king):
        if not any(moves_to(game_state, move, turn.opposite)):
            return False

    return True