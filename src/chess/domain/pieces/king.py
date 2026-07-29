from chess.domain.move_pattern import MovePattern
from chess.domain.piece import Piece


class King(Piece):
    
    def __init__(self, color):
        super().__init__(color)
        self.move_patterns.extend([
            MovePattern((1, 0), 1), 
            MovePattern((-1, 0), 1), 
            MovePattern((0, 1), 1), 
            MovePattern((0, -1), 1),
            MovePattern((1, 1), 1), 
            MovePattern((-1, 1), 1), 
            MovePattern((1, -1), 1), 
            MovePattern((-1, -1), 1)
        ])

    def __str__(self):
        return "KI" + str(self.color.value)