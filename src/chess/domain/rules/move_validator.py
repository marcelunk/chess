from chess.domain.color import Color
from chess.domain.game_state import GameState
from chess.domain.pieces.pawn import Pawn
from chess.domain.square import Square


def validate_move(source: Square, target: Square, game_state: GameState, turn: Color) -> bool:
    if not _is_inside_board(target):
        return False

    piece = game_state.get_piece(source)
    if piece is None or piece.color is not turn:
        return False

    if isinstance(piece, Pawn):
        return target in _get_pawn_legal_moves(source, game_state, piece)
    else:
        return target in _get_legal_moves(source, game_state, piece)

def _get_legal_moves(source, game_state, piece):
    legal_moves = set()

    legal_moves = legal_moves.union(_get_possible_moves(source.file, source.rank, game_state, piece))

    # TODO add rochade

    return legal_moves

def _get_possible_moves(file, rank, game_state, piece):
    color = piece.color
    legal_moves = set()
    for pattern in piece.move_patterns:
        vector = pattern.direction
        max_distance = pattern.max_distance

        for i in range(1, max_distance + 1):
            diff_file = i * vector[0]
            diff_rank = i * vector[1]
            target = Square(file + diff_file, rank + diff_rank)
            if not _is_inside_board(target):
                break

            p = game_state.get_piece(target)
            if p is not None and p.color is color:
                break
            elif p is not None and p.color is not color:
                legal_moves.add(target)
                break

            legal_moves.add(target)

    return legal_moves

def _get_pawn_legal_moves(source, game_state, pawn):
    color = pawn.color
    file = source.file
    rank = source.rank
    legal_moves = set()

    for pattern in pawn.move_patterns:
        vector = pattern.direction
        max_distance = pattern.max_distance

        if color is Color.BLACK:
            vector = (vector[0], vector[1] * -1)

        if pawn.in_start_position:
            max_distance = 2

        for i in range(1, max_distance + 1):
            diff_file = i * vector[0]
            diff_rank = i * vector[1]
            target = Square(file + diff_file, rank + diff_rank)
            if not _is_inside_board(target):
                break

            p = game_state.get_piece(target)
            if p is not None and p.color is color:
                break
            elif p is not None and p.color is not color:
                legal_moves.add(target)
                break

            legal_moves.add(target)

    hit_one = Square(file + 1, rank + vector[1])
    if _is_inside_board(hit_one) and _pawn_can_hit(game_state, color, hit_one):
        legal_moves.add(hit_one)

    hit_two = Square(file - 1, rank + vector[1])
    if _is_inside_board(hit_two) and _pawn_can_hit(game_state, color, hit_two):
        legal_moves.add(hit_two)

    en_passant_square = game_state.en_passant_square
    if _en_passant_is_allowed(en_passant_square, source):
        legal_moves.add(en_passant_square)

    # TODO add change piece

    return legal_moves

def _pawn_can_hit(game_state, color, square):
    x = game_state.get_piece(square)
    return x is not None and x.color is not color

def _en_passant_is_allowed(en_passant_square, source):
    if en_passant_square is None:
        return False
    
    one_file_difference = (en_passant_square.file - source.file) % 1 == 0
    return one_file_difference and en_passant_square.rank == source.rank

def _is_inside_board(square):
    return (square.file >= 0 and square.file < 8) and (square.rank >= 0 and square.rank < 8)