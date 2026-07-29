from dataclasses import dataclass

@dataclass(frozen=True)
class MovePattern:
    direction: tuple    # Vector
    max_distance: int
    # can_capture: bool
    # can_move_without_capture: bool