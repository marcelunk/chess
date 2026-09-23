from collections.abc import Iterator

from chess.domain.color import Color
from chess.domain.game_state import GameState
from chess.domain.move_pattern import MAX_DISTANCE, MovementPattern
from chess.domain.piece import Piece
from chess.domain.pieces.pawn import Pawn
from chess.domain.square import Square

_potential_move_vectors = [
    MovementPattern((0, 1), MAX_DISTANCE), 
    MovementPattern((1, 1), MAX_DISTANCE), 
    MovementPattern((1, 0), MAX_DISTANCE), 
    MovementPattern((1, -1), MAX_DISTANCE),
    MovementPattern((0, -1), MAX_DISTANCE), 
    MovementPattern((-1, -1), MAX_DISTANCE), 
    MovementPattern((-1, 0), MAX_DISTANCE), 
    MovementPattern((-1, 1), MAX_DISTANCE),
    MovementPattern((1, 2), 1),
    MovementPattern((2, 1), 1),
    MovementPattern((2, -1), 1),
    MovementPattern((-1, -2), 1),
    MovementPattern((-2, -1), 1),
    MovementPattern((-2, 1), 1),
    MovementPattern((-1, 2), 1),
]

def moves_to(game_state: GameState, square: Square, turn: Color) -> Iterator[Square]:
    # Yields possible moves of the given color to the given square
    for origin in _get_potential_origins(game_state, square, turn):
        for target in moves_from(game_state, origin):
            if target == square:
                yield origin

def _get_potential_origins(game_state, square, attacker):
    file = square.file
    rank = square.rank
    for vector, max_distance in _potential_move_vectors:
        for i in range(1, max_distance + 1):
            diff_file = i * vector[0]
            diff_rank = i * vector[1]
            target = Square(file + diff_file, rank + diff_rank)
            if target.is_outside_board:
                break

            occupant = game_state.get_piece(target)

            if occupant is not None and occupant.color is attacker:
                yield target

def moves_from(state: GameState, square: Square) -> Iterator[Square]:
    # Yields moves from the given field
    piece = state.get_piece(square)
    if piece is None:
        return

    if isinstance(piece, Pawn):
        yield from _moves_for_pawn(state, square, piece, piece.movement_patterns[0])
    else:
        for pattern in piece.movement_patterns:
            yield from _moves_for_pattern(state, square, piece, pattern)

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