from chess.domain.color import Color
from chess.domain.game_state import GameState
from chess.domain.move_pattern import MAX_DISTANCE, MovePattern
from chess.domain.square import Square

_move_patterns = list().extend([
            MovePattern((0, 1), MAX_DISTANCE), 
            MovePattern((1, 1), MAX_DISTANCE), 
            MovePattern((1, 0), MAX_DISTANCE), 
            MovePattern((1, -1), MAX_DISTANCE),
            MovePattern((0, -1), MAX_DISTANCE), 
            MovePattern((-1, -1), MAX_DISTANCE), 
            MovePattern((-1, 0), MAX_DISTANCE), 
            MovePattern((-1, 1), MAX_DISTANCE)
        ])

def game_state_is_check(game_state: GameState, turn: Color) -> bool:
    king_square = game_state.get_king_square(turn)
    return _is_attacked(game_state, king_square, turn.opposite)

def _is_attacked(game_state, king_square, turn):
    possible_attackers = set()
    file = king_square.file
    rank = king_square.rank
    for vector, max_distance in _move_patterns:
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

    # test possible knight attacks

    return False