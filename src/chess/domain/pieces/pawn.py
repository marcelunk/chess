from chess.domain.move_pattern import MovePattern
from chess.domain.piece import Piece
from chess.domain.square import Square


class Pawn(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.move_patterns.append(MovePattern((0, 1), 1))

    def __str__(self):
        return "PA" + str(self.color.value)