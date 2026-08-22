from abc import ABC
from dataclasses import dataclass

from chess.domain.color import Color

MAX_DISTANCE = 7

class Piece(ABC):

    def __init__(self, color: Color):
        self.color = color
        self.in_start_position = True
        self.move_patterns = list()
