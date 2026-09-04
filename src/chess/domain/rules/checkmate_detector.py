from chess.domain.color import Color
from chess.domain.game_state import GameState
from chess.domain.moves.move_generator import moves_for
from chess.domain.pieces.knight import Knight
from chess.domain.moves.square_generators import attackers_for, squares_between
from chess.domain.square import Square


def game_state_is_in_checkmate(game_state: GameState, turn: Color) -> bool:
    king_square = game_state.get_king_square(turn)
    for attacker in attackers_for(game_state, king_square, turn.opposite):
        # can the attacker be hit?
        if any(attackers_for(game_state, attacker, turn)):
            return False

        # can the attacker be blocked?
        if not isinstance(attacker, Knight):
            for square in squares_between(game_state, king_square, attacker):
                if any(attackers_for(game_state, square, turn)):
                    return False
        
        # can the king move away?
        if any(moves_for(game_state, king_square)):
            return False

    return True