from enum import Enum

class Color(Enum):
    BLACK = 0
    WHITE = 1

    @property
    def opposite(self) -> "Color":
        return Color.WHITE if self is Color.BLACK else Color.BLACK