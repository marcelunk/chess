from chess.domain.color import Color
from chess.domain.game_state import GameState
from chess.domain.moves.move_generator import moves_for
from chess.domain.pieces.knight import Knight
from chess.domain.rules.square_validator import square_is_attacked
from chess.domain.square import Square


def game_state_is_in_checkmate(game_state: GameState, position_attacker: Square, turn: Color) -> bool:
    # can attacker be hit?
    if square_is_attacked(game_state, position_attacker):
        return False

    # can attacker be blocked?
    attacker = game_state.get_piece(position_attacker)
    if not isinstance(attacker, Knight):
        # If attacker is not knight: check all square on the attack vector with square_can_be_reached
        pass
    
    # can king move away?
    king_square = game_state.get_king_square(turn)
    for move in moves_for(game_state, king_square):
        if not square_is_attacked(game_state, move, turn):
            return True