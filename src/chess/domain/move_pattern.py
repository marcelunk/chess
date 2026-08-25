from dataclasses import dataclass

MAX_DISTANCE = 7

@dataclass(frozen=True)
class MovePattern:
    vector: tuple 
    max_distance: int

    def __iter__(self):
        yield self.vector
        yield self.max_distance