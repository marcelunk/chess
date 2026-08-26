from chess.domain.color import Color
from chess.domain.game_state import GameState
from chess.domain.moves.move_generator import moves_for
from chess.domain.square import Square


# Ist dieser konkrete Zug nach allen Schachregeln legal?
def validate_move(source: Square, target: Square, game_state: GameState, turn: Color) -> bool:
    if source.is_outside_board or target.is_outside_board:
        return False

    piece = game_state.get_piece(source)
    if piece is None or piece.color is not turn:
        return False

    for move in moves_for(game_state, source):
        if move is target:
            return True

    

    # possible_capture_one = Square(file + 1, rank + vector[1])
    # if possible_capture_one.is_inside_board and _pawn_can_capture(game_state, color, possible_capture_one):
    #     legal_moves.add(possible_capture_one)

    # possible_capture_two = Square(file - 1, rank + vector[1])
    # if possible_capture_two.is_inside_board and _pawn_can_capture(game_state, color, possible_capture_two):
    #     legal_moves.add(possible_capture_two)

    # en_passant_square = game_state.en_passant_square
    # if _en_passant_is_allowed(en_passant_square, source, pawn):
    #     legal_moves.add(en_passant_square)

    return False

def _get_moves(source, game_state, piece):
    color = piece.color
    file = source.file
    rank = source.rank

    legal_moves = set()
    for pattern in piece.movement_patterns:
        legal_moves = legal_moves.union(_get_moves_from_vector(game_state, color, file, rank, pattern.vector, pattern.max_distance))

    return legal_moves

def _get_moves_pawn(source, game_state, pawn):
    color = pawn.color
    file = source.file
    rank = source.rank
    legal_moves = set()

    for vector, max_distance in pawn.movement_patterns:
        if color is Color.BLACK:
            vector = (vector[0], vector[1] * -1)

        if pawn.in_start_position:
            max_distance = 2

        legal_moves = legal_moves.union(_get_moves_from_vector(game_state, color, file, rank, vector, max_distance))

    possible_capture_one = Square(file + 1, rank + vector[1])
    if possible_capture_one.is_inside_board and _pawn_can_capture(game_state, color, possible_capture_one):
        legal_moves.add(possible_capture_one)

    possible_capture_two = Square(file - 1, rank + vector[1])
    if possible_capture_two.is_inside_board and _pawn_can_capture(game_state, color, possible_capture_two):
        legal_moves.add(possible_capture_two)

    en_passant_square = game_state.en_passant_square
    if _en_passant_is_allowed(en_passant_square, source, pawn):
        legal_moves.add(en_passant_square)

    return legal_moves

def _get_moves_from_vector(game_state, color, file, rank, vector, max_distance):
    legal_moves = set()
    for i in range(1, max_distance + 1):
        diff_file = i * vector[0]
        diff_rank = i * vector[1]
        target = Square(file + diff_file, rank + diff_rank)
        if target.is_outside_board:
            break

        p = game_state.get_piece(target)
        if p is not None and p.color is color:
            break
        elif p is not None and p.color is not color:
            legal_moves.add(target)
            break

        legal_moves.add(target)

    return legal_moves

def _pawn_can_capture(game_state, color, square):
    x = game_state.get_piece(square)
    return x is not None and x.color is not color

def _en_passant_is_allowed(en_passant_square, source, pawn):
    if en_passant_square is None:
        return False

    move_pattern = pawn.movement_patterns[0]
    new_rank = None
    if pawn.color is Color.WHITE:
        new_rank = source.rank + move_pattern.vector[1]
    else:
        new_rank = source.rank - move_pattern.vector[1]

    possible_en_passant_squares = set()
    possible_en_passant_squares.add(Square(source.file + 1, new_rank))
    possible_en_passant_squares.add(Square(source.file - 1, new_rank))
    
    return en_passant_square in possible_en_passant_squares