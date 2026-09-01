from chess.domain.color import Color
from chess.domain.game_state import GameState
from chess.domain.move_pattern import MAX_DISTANCE, MovementPattern
from chess.domain.moves.move_generator import moves_for
from chess.domain.square import Square

_potential_attack_vectors = [
    MovementPattern((0, 1), MAX_DISTANCE), 
    MovementPattern((1, 1), MAX_DISTANCE), 
    MovementPattern((1, 0), MAX_DISTANCE), 
    MovementPattern((1, -1), MAX_DISTANCE),
    MovementPattern((0, -1), MAX_DISTANCE), 
    MovementPattern((-1, -1), MAX_DISTANCE), 
    MovementPattern((-1, 0), MAX_DISTANCE), 
    MovementPattern((-1, 1), MAX_DISTANCE),
    MovementPattern((1, 2), 1),
    MovementPattern((2, 1), 1),
    MovementPattern((2, -1), 1),
    MovementPattern((-1, -2), 1),
    MovementPattern((-2, -1), 1),
    MovementPattern((-2, 1), 1),
    MovementPattern((-1, 2), 1),
]

def game_state_is_in_check(game_state: GameState, turn: Color) -> bool:
    # checks if the king of this turn is in check according to the given game state
    # TODO does not consider check due to en passant 
    king_square = game_state.get_king_square(turn)
    return _is_attacked(game_state, king_square, turn)

def _is_attacked(game_state, king_square, turn):
    for origin_attacker in _get_potential_attackers(game_state, king_square, turn):
        for threaten in moves_for(game_state, origin_attacker):
            if threaten == king_square:
                return True

    return False

def _get_potential_attackers(game_state, king_square, turn):
    file = king_square.file
    rank = king_square.rank
    for vector, max_distance in _potential_attack_vectors:
        for i in range(1, max_distance + 1):
            diff_file = i * vector[0]
            diff_rank = i * vector[1]
            target = Square(file + diff_file, rank + diff_rank)
            if target.is_outside_board:
                break

            occupant = game_state.get_piece(target)

            if occupant is not None and occupant.color is not turn:
                yield target