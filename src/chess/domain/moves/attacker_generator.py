from collections.abc import Iterator

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

def attackers_for(game_state: GameState, square: Square, attacker: Color) -> Iterator[Square]:
    for origin_attacker in _get_potential_attackers(game_state, square, attacker):
        for threaten in moves_for(game_state, origin_attacker):
            if threaten == square:
                yield origin_attacker

def _get_potential_attackers(game_state, square, attacker):
    file = square.file
    rank = square.rank
    for vector, max_distance in _potential_attack_vectors:
        for i in range(1, max_distance + 1):
            diff_file = i * vector[0]
            diff_rank = i * vector[1]
            target = Square(file + diff_file, rank + diff_rank)
            if target.is_outside_board:
                break

            occupant = game_state.get_piece(target)

            if occupant is not None and occupant.color is attacker:
                yield target