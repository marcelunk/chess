from abc import ABC
from chess.domain.color import Color

class Piece(ABC):

    def __init__(self, color: Color):
        self.color = color
        self.in_start_position = True
        self.movement_patterns = list()
