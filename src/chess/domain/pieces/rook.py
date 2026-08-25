from chess.domain.move_pattern import MAX_DISTANCE, MovementPattern
from chess.domain.piece import Piece


class Rook(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.movement_patterns.extend([
            MovementPattern((1, 0), MAX_DISTANCE), 
            MovementPattern((-1, 0), MAX_DISTANCE), 
            MovementPattern((0, 1), MAX_DISTANCE), 
            MovementPattern((0, -1), MAX_DISTANCE)
        ])

    def __str__(self):
        return "R" + str(self.color.value)