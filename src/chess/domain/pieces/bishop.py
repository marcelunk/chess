from chess.domain.move_pattern import MovePattern
from chess.domain.piece import MAX_DISTANCE, Piece


class Bishop(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.move_patterns.extend([
            MovePattern((1, 1), MAX_DISTANCE), 
            MovePattern((-1, 1), MAX_DISTANCE), 
            MovePattern((1, -1), MAX_DISTANCE), 
            MovePattern((-1, -1), MAX_DISTANCE)
        ])

    def __str__(self):
        return "BI" + str(self.color.value)