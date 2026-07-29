from chess.domain.move_pattern import MovePattern
from chess.domain.piece import Piece


class Knight(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.move_patterns.extend([
            MovePattern((2, 1), 1), 
            MovePattern((2, -1), 1), 
            MovePattern((-2, 1), 1), 
            MovePattern((-2, -1), 1),
            MovePattern((1, 2), 1), 
            MovePattern((1, -2), 1), 
            MovePattern((-1, 2), 1), 
            MovePattern((-1, -2), 1)
        ])

    def __str__(self):
        return "KN" + str(self.color.value)