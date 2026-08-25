from chess.domain.move_pattern import MAX_DISTANCE, MovementPattern
from chess.domain.piece import Piece


class Bishop(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.movement_patterns.extend([
            MovementPattern((1, 1), MAX_DISTANCE), 
            MovementPattern((-1, 1), MAX_DISTANCE), 
            MovementPattern((1, -1), MAX_DISTANCE), 
            MovementPattern((-1, -1), MAX_DISTANCE)
        ])

    def __str__(self):
        return "B" + str(self.color.value)