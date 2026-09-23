from chess.domain.color import Color
from chess.domain.game_state import GameState
from chess.domain.moves.move_generator import moves_to

def game_state_is_in_check(game_state: GameState, turn: Color) -> bool:
    # checks if the king of this turn is in check according to the given game state
    king_square = game_state.get_king_square(turn)
    for attacker in moves_to(game_state, king_square, turn.opposite):
        return True

    return False