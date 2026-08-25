from chess.domain.move_pattern import MovementPattern
from chess.domain.piece import Piece


class King(Piece):
    
    def __init__(self, color):
        super().__init__(color)
        self.movement_patterns.extend([
            MovementPattern((1, 0), 1), 
            MovementPattern((-1, 0), 1), 
            MovementPattern((0, 1), 1), 
            MovementPattern((0, -1), 1),
            MovementPattern((1, 1), 1), 
            MovementPattern((-1, 1), 1), 
            MovementPattern((1, -1), 1), 
            MovementPattern((-1, -1), 1)
        ])

    def __str__(self):
        return "K" + str(self.color.value)