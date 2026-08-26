from abc import ABC
from chess.domain.color import Color

class Piece(ABC):

    def __init__(self, color: Color):
        self.color = color
        self.in_start_position = True
        self.movement_patterns = list()

    @property
    def is_dark(self) -> bool:
        return self.color is Color.BLACK

    @property
    def is_light(self) -> bool:
        return not self.is_dark