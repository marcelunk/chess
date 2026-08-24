from dataclasses import dataclass

@dataclass(frozen=True)
class MovePattern:
    vector: tuple 
    max_distance: int