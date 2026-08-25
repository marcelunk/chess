from collections.abc import Iterator

from chess.domain.game_state import GameState
from chess.domain.move_pattern import MovementPattern
from chess.domain.piece import Piece
from chess.domain.square import Square


class MoveGenerator:

    def moves_for(self, state: GameState, square: Square) -> Iterator[Square]:
        piece = state.get_piece(square)

        for pattern in piece.movement_patterns:
            yield from self._moves_for_pattern(state, square, piece, pattern)

    def _moves_for_pattern(self, state: GameState, origin: Square, piece: Piece, pattern: MovementPattern) -> Iterator[Square]:
        vector = pattern.vector
        max_distance = pattern.max_distance
        file = origin.file
        rank = origin.rank
        for i in range(1, max_distance + 1):
            diff_file = i * vector[0]
            diff_rank = i * vector[1]
            target = Square(file + diff_file, rank + diff_rank)

            if target.is_outside_board:
                break

            occupant = state.piece_at(target)

            if occupant is None:
                yield target
            elif occupant.color is not piece.color:
                yield target
                break
            else:
                break