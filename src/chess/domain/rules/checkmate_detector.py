from chess.domain.color import Color
from chess.domain.game_state import GameState
from chess.domain.moves.move_generator import moves_from, moves_to
from chess.domain.pieces.knight import Knight
from chess.domain.moves.square_utilities import squares_between


def game_state_is_in_checkmate(game_state: GameState, turn: Color) -> bool:
    king_square = game_state.get_king_square(turn)
    for origin_attacker in moves_to(game_state, king_square, turn.opposite):
        # can the attacker be hit?
        if any(moves_to(game_state, origin_attacker, turn)):
            return False

        # can the attacker be blocked?
        if not isinstance(origin_attacker, Knight):
            for square in squares_between(game_state, king_square, origin_attacker):
                if any(moves_from(game_state, square, turn)):
                    return False
        
        # can the king move away?
        if any(moves_from(game_state, king_square)):
            return False

    return True