from abc import ABC

MAX_DISTANCE = 7

class Piece(ABC):

    def __init__(self, color):
        self.color = color
        self.in_start_position = True
        self.move_patterns = list()
