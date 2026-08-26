from chess.domain.move_pattern import MovementPattern
from chess.domain.piece import Piece


class Pawn(Piece):

    def __init__(self, color):
        super().__init__(color)
        if self.is_dark:
            self.movement_patterns.append(MovementPattern((0, -1), 1))
        else:
            self.movement_patterns.append(MovementPattern((0, 1), 1))

    def __str__(self):
        return "P" + str(self.color.value)


    # TODO yield movement_patterns with generator?