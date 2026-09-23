from collections.abc import Iterator

from chess.domain.square import Square

def squares_between(square_a: Square, square_b: Square) -> Iterator[Square]:
    # Yields squares between the two given squares if they lie in a straight line
    if square_a == square_b:
        return
    
    distances = get_distance(square_a, square_b)

    if 0 not in distances:
        quotient = abs(round(distances[0] / distances[1], 1))
        if not (quotient == 0.0 or quotient == 1.0):
            return

    step_file = _get_step(distances[0])
    step_rank = _get_step(distances[1])
    square = square_a
    while True:
        square = Square(square.file + step_file, square.rank + step_rank)

        if square == square_b:
            break

        yield square

def get_distance(source: Square, target: Square) -> tuple:
    x = target.file - source.file
    y = target.rank - source.rank
    return (x, y)

def _get_step(distance):
    if distance == 0:
        return 0
    elif distance > 0:
        return 1
    elif distance < 0:
        return -1