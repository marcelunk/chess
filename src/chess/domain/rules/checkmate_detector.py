from chess.domain.color import Color
from chess.domain.game_state import GameState
from chess.domain.moves.move_generator import moves_for
from chess.domain.pieces.knight import Knight
from chess.domain.moves.attacker_generator import attackers_for
from chess.domain.square import Square


def game_state_is_in_checkmate(game_state: GameState, turn: Color) -> bool:
    king_square = game_state.get_king_square(turn)
    for attacker in attackers_for(game_state, king_square, turn.opposite):
        # can the attacker be hit?
        pass

        # can the attacker be blocked?
        if not isinstance(attacker, Knight):
            # If attacker is not knight: check all square on the attack vector with square_can_be_reached
            pass
        
        # can the king move away?
        king_square = game_state.get_king_square(turn)
        for move in moves_for(game_state, king_square):
            for attacker in attackers_for(game_state, move, turn.opposite):
                pass