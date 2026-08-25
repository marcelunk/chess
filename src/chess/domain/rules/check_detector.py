from chess.domain.color import Color
from chess.domain.game_state import GameState
from chess.domain.move_pattern import MAX_DISTANCE, MovePattern
from chess.domain.square import Square

_attack_vectors = list().extend([
    MovePattern((0, 1), MAX_DISTANCE), 
    MovePattern((1, 1), MAX_DISTANCE), 
    MovePattern((1, 0), MAX_DISTANCE), 
    MovePattern((1, -1), MAX_DISTANCE),
    MovePattern((0, -1), MAX_DISTANCE), 
    MovePattern((-1, -1), MAX_DISTANCE), 
    MovePattern((-1, 0), MAX_DISTANCE), 
    MovePattern((-1, 1), MAX_DISTANCE),
    MovePattern((1, 2), 1),
    MovePattern((2, 1), 1),
    MovePattern((2, -1), 1),
    MovePattern((-1, -2), 1),
    MovePattern((-2, -1), 1),
    MovePattern((-2, 1), 1),
    MovePattern((-1, 2), 1),
])

def game_state_is_in_check(game_state: GameState, turn: Color) -> bool:
    king_square = game_state.get_king_square(turn)
    return _is_attacked(game_state, king_square, turn.opposite)

def _is_attacked(game_state, king_square, turn):
    possible_attackers = _get_possible_attackers(game_state, king_square, turn)
    for source in possible_attackers:
        if _can_capture(source, king_square, game_state):
            return True

    return False

def _get_possible_attackers(game_state, king_square, turn):
    possible_attackers = set()
    file = king_square.file
    rank = king_square.rank
    for vector, max_distance in _attack_vectors:
        for i in range(1, max_distance + 1):
            diff_file = i * vector[0]
            diff_rank = i * vector[1]
            target = Square(file + diff_file, rank + diff_rank)
            if target.is_outside_board:
                break

            piece = game_state.get_piece(target)
            if piece is not None:
                if piece.color is turn:
                    break
                else:
                    possible_attackers.add(target)
                    break

    return possible_attackers

def _can_capture(source, target, game_state):
    piece = game_state.get_piece(source)
    file = source.file
    rank = source.rank
    for vector, max_distance in piece.move_patterns:
        for i in range(1, max_distance + 1):
            diff_file = i * vector[0]
            diff_rank = i * vector[1]
            next = Square(file + diff_file, rank + diff_rank)

            if next.is_outside_board:
                break

            if next is target:
                return True

    return False