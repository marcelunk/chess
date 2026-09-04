from chess.domain.color import Color
from chess.domain.game_state import GameState
from chess.domain.moves.attacker_generator import attackers_for

def game_state_is_in_check(game_state: GameState, turn: Color) -> bool:
    # checks if the king of this turn is in check according to the given game state
    king_square = game_state.get_king_square(turn)
    for attacker in attackers_for(game_state, king_square, turn.opposite):
        return True

    return False