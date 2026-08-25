from chess.domain.move_pattern import MovementPattern
from chess.domain.piece import Piece


class Knight(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.movement_patterns.extend([
            MovementPattern((2, 1), 1), 
            MovementPattern((2, -1), 1), 
            MovementPattern((-2, 1), 1), 
            MovementPattern((-2, -1), 1),
            MovementPattern((1, 2), 1), 
            MovementPattern((1, -2), 1), 
            MovementPattern((-1, 2), 1), 
            MovementPattern((-1, -2), 1)
        ])

    def __str__(self):
        return "KN" + str(self.color.value)