from chess.domain.move_pattern import MovementPattern
from chess.domain.piece import Piece


class Pawn(Piece):

    def __init__(self, color):
        super().__init__(color)
        pattern = MovementPattern((0, -1), 1) if self.is_dark else MovementPattern((0, 1), 1)
        self.movement_patterns.append(pattern)

    def __str__(self):
        return "P" + str(self.color.value)


    # TODO yield movement_patterns with generator?