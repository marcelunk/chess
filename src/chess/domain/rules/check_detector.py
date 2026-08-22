from chess.domain.color import Color
from chess.domain.game_state import GameState


def game_state_is_check(game_state: GameState, turn: Color) -> bool:
    king_square = game_state.get_king_square(turn)
    return _is_attacked(game_state, king_square, turn.opposite)

def _is_attacked(game_state, king_square, turn):
    # test all directions from king square and see if reached piece threats king
    
    # test possible knight attacks

    return False