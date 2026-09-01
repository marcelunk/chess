from chess.domain.color import Color
from chess.domain.game_state import GameState
from chess.domain.moves.move_generator import moves_for
from chess.domain.pieces.pawn import Pawn
from chess.domain.rules.check_detector import game_state_is_in_check
from chess.domain.square import Square


def validate_move(source: Square, target: Square, game_state: GameState, turn: Color) -> bool:
    # Validates this move according to chess rules    
    if source.is_outside_board or target.is_outside_board:
        return False

    piece = game_state.get_piece(source)
    if piece is None or piece.color is not turn:
        return False

    for move in moves_for(game_state, source):
        if move == target:
            new_game_state = game_state.make_move(source, target)
            return False if game_state_is_in_check(new_game_state, turn) else True
            

    if isinstance(piece, Pawn) and _en_passant_is_allowed(game_state.en_passant_square, source, piece.movement_patterns[0]):
        new_game_state = game_state.make_move(source, target)
        return False if game_state_is_in_check(new_game_state, turn) else True

    return False

def _en_passant_is_allowed(en_passant_square, source, pattern):
    if en_passant_square is None:
        return False

    new_rank = source.rank + pattern.vector[1]
    possible_en_passant_squares = set()
    possible_en_passant_squares.add(Square(source.file + 1, new_rank))
    possible_en_passant_squares.add(Square(source.file - 1, new_rank))
    
    return en_passant_square in possible_en_passant_squares