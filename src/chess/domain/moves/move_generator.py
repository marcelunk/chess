from collections.abc import Iterator

from chess.domain.game_state import GameState
from chess.domain.move_pattern import MovementPattern
from chess.domain.piece import Piece
from chess.domain.pieces.pawn import Pawn
from chess.domain.square import Square

def moves_for(state: GameState, square: Square) -> Iterator[Square]:
    # Yields moves which are possible according to the given game state and piece
    piece = state.get_piece(square)

    if isinstance(piece, Pawn):
        yield from _moves_for_pawn(state, square, piece, piece.movement_patterns[0])
    else:
        for pattern in piece.movement_patterns:
            yield from _moves_for_pattern(state, square, piece, pattern) # TODO maybe not yield from?

def _moves_for_pattern(state: GameState, origin: Square, piece: Piece, pattern: MovementPattern) -> Iterator[Square]:
    file = origin.file
    rank = origin.rank
    vector = pattern.vector
    max_distance = pattern.max_distance
    
    for i in range(1, max_distance + 1):
        diff_file = i * vector[0]
        diff_rank = i * vector[1]
        target = Square(file + diff_file, rank + diff_rank)

        if target.is_outside_board:
            break

        occupant = state.get_piece(target)

        if occupant is None:
            yield target
        elif occupant.color is not piece.color:
            yield target
            break
        else:
            break

def _moves_for_pawn(state: GameState, origin: Square, pawn: Pawn, pattern: MovementPattern) -> Iterator[Square]:
    file = origin.file
    rank = origin.rank
    vector = pattern.vector
    max_distance = pattern.max_distance

    if pawn.in_start_position:
        max_distance = 2

    capture_one = Square(file + 1, rank + vector[1] * 1)
    if capture_one.is_inside_board and state.is_occupied(capture_one):
        yield capture_one

    capture_two = Square(file - 1, rank + vector[1] * 1)
    if capture_two.is_inside_board and state.is_occupied(capture_two):
        yield capture_two

    for i in range(1, max_distance + 1):
        diff_file = i * vector[0]
        diff_rank = i * vector[1]
        target = Square(file + diff_file, rank + diff_rank)

        if target.is_outside_board:
            break

        occupant = state.get_piece(target)

        if occupant is None:
            yield target
        elif occupant.color is not pawn.color:
            yield target
            break
        else:
            break