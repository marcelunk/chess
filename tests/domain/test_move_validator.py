from chess.domain.color import Color
from chess.domain.game_state import GameStateFactory
from chess.domain.pieces.bishop import Bishop
from chess.domain.pieces.king import King
from chess.domain.pieces.knight import Knight
from chess.domain.pieces.pawn import Pawn
from chess.domain.pieces.queen import Queen
from chess.domain.pieces.rook import Rook
from chess.domain.rules.move_validator import validate_move
from chess.domain.square import Square

# Pawn test cases
def test_pawn_can_move_one_square_straight():
    game_state = GameStateFactory.create_empty_game_state()
    game_state.place_piece(Pawn(Color.WHITE), Square(0, 1))
    is_valid = validate_move(Square(0, 1), Square(0, 2), game_state, Color.WHITE)
    assert is_valid

def test_pawn_can_move_two_squares_straight_from_initial_position():
    game_state = GameStateFactory.create_empty_game_state()
    game_state.place_piece(Pawn(Color.WHITE), Square(0, 1))
    is_valid = validate_move(Square(0, 1), Square(0, 3), game_state, Color.WHITE)
    assert is_valid

def test_white_pawn_can_hit_black_diagonal():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(1, 1)
    target_1 = Square(2, 2)
    target_2 = Square(0, 2)
    game_state.place_piece(Pawn(Color.WHITE), source)
    game_state.place_piece(Rook(Color.BLACK), target_1)
    game_state.place_piece(Bishop(Color.BLACK), target_2)
    assert validate_move(source, target_1, game_state, Color.WHITE)
    assert validate_move(source, target_2, game_state, Color.WHITE)

def test_white_pawn_can_not_move_more_than_one_square_straight():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(0, 1)
    target = Square(0, 4)
    game_state.place_piece(Pawn(Color.WHITE), source)
    is_valid = validate_move(source, target, game_state, Color.WHITE)
    assert not is_valid

def test_white_pawn_can_not_move_diagonal_to_empty_square():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(1, 1)
    target_1 = Square(0, 2)
    target_2 = Square(2, 2)
    game_state.place_piece(Pawn(Color.WHITE), source)
    assert not validate_move(source, target_1, game_state, Color.WHITE)
    assert not validate_move(source, target_2, game_state, Color.WHITE)

def test_white_pawn_can_not_move_backwards():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(1, 1)
    target = Square(1, 0)
    game_state.place_piece(Pawn(Color.WHITE), source)
    assert not validate_move(source, target, game_state, Color.WHITE)

def test_white_pawn_can_not_move_sideways():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(1, 1)
    target_1 = Square(0, 1)
    target_2 = Square(2, 1)
    game_state.place_piece(Pawn(Color.WHITE), source)
    assert not validate_move(source, target_1, game_state, Color.WHITE)
    assert not validate_move(source, target_2, game_state, Color.WHITE)

def test_white_pawn_can_not_move_diagonal():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(1, 1)
    game_state.place_piece(Pawn(Color.WHITE), source)
    assert not validate_move(source, Square(2, 2), game_state, Color.WHITE)
    assert not validate_move(source, Square(0, 2), game_state, Color.WHITE)
    assert not validate_move(source, Square(0, 0), game_state, Color.WHITE)
    assert not validate_move(source, Square(2, 0), game_state, Color.WHITE)

def test_white_pawn_can_not_move_to_occupied_by_white():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(1, 1)
    target = Square(1, 2)
    game_state.place_piece(Pawn(Color.WHITE), source)
    game_state.place_piece(Rook(Color.WHITE), target)
    assert not validate_move(source, target, game_state, Color.WHITE)

def test_white_pawn_can_not_move_outside_of_board():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(0, 7)
    target = Square(0, 8)
    game_state.place_piece(Pawn(Color.WHITE), source)
    assert not validate_move(source, target, game_state, Color.WHITE)

# Rook test cases
def test_rook_can_only_move_in_straight_lines():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(3, 3)
    game_state.place_piece(Rook(Color.WHITE), source)
    assert validate_move(source, Square(3, 4), game_state, Color.WHITE)
    assert validate_move(source, Square(3, 5), game_state, Color.WHITE)
    assert validate_move(source, Square(3, 6), game_state, Color.WHITE)
    assert validate_move(source, Square(3, 7), game_state, Color.WHITE)
    assert validate_move(source, Square(2, 3), game_state, Color.WHITE)
    assert validate_move(source, Square(1, 3), game_state, Color.WHITE)
    assert validate_move(source, Square(0, 3), game_state, Color.WHITE)
    assert validate_move(source, Square(4, 3), game_state, Color.WHITE)
    assert validate_move(source, Square(5, 3), game_state, Color.WHITE)
    assert validate_move(source, Square(6, 3), game_state, Color.WHITE)
    assert validate_move(source, Square(7, 3), game_state, Color.WHITE)
    assert validate_move(source, Square(3, 2), game_state, Color.WHITE)
    assert validate_move(source, Square(3, 1), game_state, Color.WHITE)
    assert validate_move(source, Square(3, 0), game_state, Color.WHITE)

def test_some_blind_spots_of_rook():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(3, 3)
    game_state.place_piece(Rook(Color.WHITE), source)
    assert not validate_move(source, Square(4, 7), game_state, Color.WHITE)
    assert not validate_move(source, Square(7, 0), game_state, Color.WHITE)
    assert not validate_move(source, Square(2, 7), game_state, Color.WHITE)

def test_rook_can_not_move_outside_of_board():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(3, 3)
    game_state.place_piece(Rook(Color.WHITE), source)
    assert not validate_move(source, Square(3, 8), game_state, Color.WHITE)
    assert not validate_move(source, Square(-1, 3), game_state, Color.WHITE)
    assert not validate_move(source, Square(8, 3), game_state, Color.WHITE)
    assert not validate_move(source, Square(3, -1), game_state, Color.WHITE)

def test_rook_can_not_move_diagonal():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(3, 3)
    game_state.place_piece(Rook(Color.WHITE), source)
    assert not validate_move(source, Square(4, 2), game_state, Color.WHITE)
    assert not validate_move(source, Square(5, 1), game_state, Color.WHITE)
    assert not validate_move(source, Square(6, 0), game_state, Color.WHITE)
    assert not validate_move(source, Square(2, 2), game_state, Color.WHITE)
    assert not validate_move(source, Square(1, 1), game_state, Color.WHITE)
    assert not validate_move(source, Square(0, 0), game_state, Color.WHITE)
    assert not validate_move(source, Square(2, 4), game_state, Color.WHITE)
    assert not validate_move(source, Square(1, 5), game_state, Color.WHITE)
    assert not validate_move(source, Square(0, 6), game_state, Color.WHITE)
    assert not validate_move(source, Square(4, 4), game_state, Color.WHITE)
    assert not validate_move(source, Square(5, 5), game_state, Color.WHITE)
    assert not validate_move(source, Square(6, 6), game_state, Color.WHITE)
    assert not validate_move(source, Square(7, 7), game_state, Color.WHITE)

# Bishop test cases
def test_bishop_can_only_move_diagonal():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(3, 3)
    game_state.place_piece(Bishop(Color.WHITE), source)
    assert validate_move(source, Square(4, 2), game_state, Color.WHITE)
    assert validate_move(source, Square(5, 1), game_state, Color.WHITE)
    assert validate_move(source, Square(6, 0), game_state, Color.WHITE)
    assert validate_move(source, Square(2, 2), game_state, Color.WHITE)
    assert validate_move(source, Square(1, 1), game_state, Color.WHITE)
    assert validate_move(source, Square(0, 0), game_state, Color.WHITE)
    assert validate_move(source, Square(2, 4), game_state, Color.WHITE)
    assert validate_move(source, Square(1, 5), game_state, Color.WHITE)
    assert validate_move(source, Square(0, 6), game_state, Color.WHITE)
    assert validate_move(source, Square(4, 4), game_state, Color.WHITE)
    assert validate_move(source, Square(5, 5), game_state, Color.WHITE)
    assert validate_move(source, Square(6, 6), game_state, Color.WHITE)
    assert validate_move(source, Square(7, 7), game_state, Color.WHITE)

def test_bishop_can_not_move_in_straight_lines():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(3, 3)
    game_state.place_piece(Bishop(Color.WHITE), source)
    assert not validate_move(source, Square(3, 4), game_state, Color.WHITE)
    assert not validate_move(source, Square(3, 5), game_state, Color.WHITE)
    assert not validate_move(source, Square(3, 6), game_state, Color.WHITE)
    assert not validate_move(source, Square(3, 7), game_state, Color.WHITE)
    assert not validate_move(source, Square(2, 3), game_state, Color.WHITE)
    assert not validate_move(source, Square(1, 3), game_state, Color.WHITE)
    assert not validate_move(source, Square(0, 3), game_state, Color.WHITE)
    assert not validate_move(source, Square(4, 3), game_state, Color.WHITE)
    assert not validate_move(source, Square(5, 3), game_state, Color.WHITE)
    assert not validate_move(source, Square(6, 3), game_state, Color.WHITE)
    assert not validate_move(source, Square(7, 3), game_state, Color.WHITE)
    assert not validate_move(source, Square(3, 2), game_state, Color.WHITE)
    assert not validate_move(source, Square(3, 1), game_state, Color.WHITE)
    assert not validate_move(source, Square(3, 0), game_state, Color.WHITE)

def test_bishop_can_not_move_outside_of_board():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(3, 3)
    game_state.place_piece(Bishop(Color.WHITE), source)
    assert not validate_move(source, Square(8, 8), game_state, Color.WHITE)
    assert not validate_move(source, Square(8, -1), game_state, Color.WHITE)
    assert not validate_move(source, Square(-1, -1), game_state, Color.WHITE)
    assert not validate_move(source, Square(-1, 8), game_state, Color.WHITE)

# Knight test cases
def test_knight_can_move_to_eight_fields():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(3, 3)
    game_state.place_piece(Knight(Color.WHITE), source)
    assert validate_move(source, Square(2, 1), game_state, Color.WHITE)
    assert validate_move(source, Square(1, 2), game_state, Color.WHITE)
    assert validate_move(source, Square(1, 4), game_state, Color.WHITE)
    assert validate_move(source, Square(2, 5), game_state, Color.WHITE)
    assert validate_move(source, Square(4, 5), game_state, Color.WHITE)
    assert validate_move(source, Square(5, 4), game_state, Color.WHITE)
    assert validate_move(source, Square(5, 2), game_state, Color.WHITE)
    assert validate_move(source, Square(4, 1), game_state, Color.WHITE)

def test_knight_can_not_move_outside_board():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(1, 1)
    game_state.place_piece(Knight(Color.WHITE), source)
    assert not validate_move(source, Square(0, -1), game_state, Color.WHITE)
    assert not validate_move(source, Square(-1, 0), game_state, Color.WHITE)
    assert not validate_move(source, Square(-1, 2), game_state, Color.WHITE)

def test_knight_can_not_move_straight():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(3, 3)
    game_state.place_piece(Knight(Color.WHITE), source)
    assert not validate_move(source, Square(3, 4), game_state, Color.WHITE)
    assert not validate_move(source, Square(3, 5), game_state, Color.WHITE)
    assert not validate_move(source, Square(3, 6), game_state, Color.WHITE)
    assert not validate_move(source, Square(3, 7), game_state, Color.WHITE)
    assert not validate_move(source, Square(2, 3), game_state, Color.WHITE)
    assert not validate_move(source, Square(1, 3), game_state, Color.WHITE)
    assert not validate_move(source, Square(0, 3), game_state, Color.WHITE)
    assert not validate_move(source, Square(4, 3), game_state, Color.WHITE)
    assert not validate_move(source, Square(5, 3), game_state, Color.WHITE)
    assert not validate_move(source, Square(6, 3), game_state, Color.WHITE)
    assert not validate_move(source, Square(7, 3), game_state, Color.WHITE)
    assert not validate_move(source, Square(3, 2), game_state, Color.WHITE)
    assert not validate_move(source, Square(3, 1), game_state, Color.WHITE)
    assert not validate_move(source, Square(3, 0), game_state, Color.WHITE)

def test_knight_can_not_move_diagonal():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(3, 3)
    game_state.place_piece(Knight(Color.WHITE), source)
    assert not validate_move(source, Square(4, 2), game_state, Color.WHITE)
    assert not validate_move(source, Square(5, 1), game_state, Color.WHITE)
    assert not validate_move(source, Square(6, 0), game_state, Color.WHITE)
    assert not validate_move(source, Square(2, 2), game_state, Color.WHITE)
    assert not validate_move(source, Square(1, 1), game_state, Color.WHITE)
    assert not validate_move(source, Square(0, 0), game_state, Color.WHITE)
    assert not validate_move(source, Square(2, 4), game_state, Color.WHITE)
    assert not validate_move(source, Square(1, 5), game_state, Color.WHITE)
    assert not validate_move(source, Square(0, 6), game_state, Color.WHITE)
    assert not validate_move(source, Square(4, 4), game_state, Color.WHITE)
    assert not validate_move(source, Square(5, 5), game_state, Color.WHITE)
    assert not validate_move(source, Square(6, 6), game_state, Color.WHITE)
    assert not validate_move(source, Square(7, 7), game_state, Color.WHITE)

# Queen test cases
def test_queen_can_move_straight():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(3, 3)
    game_state.place_piece(Queen(Color.WHITE), source)
    assert validate_move(source, Square(3, 4), game_state, Color.WHITE)
    assert validate_move(source, Square(3, 5), game_state, Color.WHITE)
    assert validate_move(source, Square(3, 6), game_state, Color.WHITE)
    assert validate_move(source, Square(3, 7), game_state, Color.WHITE)
    assert validate_move(source, Square(2, 3), game_state, Color.WHITE)
    assert validate_move(source, Square(1, 3), game_state, Color.WHITE)
    assert validate_move(source, Square(0, 3), game_state, Color.WHITE)
    assert validate_move(source, Square(4, 3), game_state, Color.WHITE)
    assert validate_move(source, Square(5, 3), game_state, Color.WHITE)
    assert validate_move(source, Square(6, 3), game_state, Color.WHITE)
    assert validate_move(source, Square(7, 3), game_state, Color.WHITE)
    assert validate_move(source, Square(3, 2), game_state, Color.WHITE)
    assert validate_move(source, Square(3, 1), game_state, Color.WHITE)
    assert validate_move(source, Square(3, 0), game_state, Color.WHITE)

def test_queen_can_move_diagonal():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(3, 3)
    game_state.place_piece(Queen(Color.WHITE), source)
    assert validate_move(source, Square(4, 2), game_state, Color.WHITE)
    assert validate_move(source, Square(5, 1), game_state, Color.WHITE)
    assert validate_move(source, Square(6, 0), game_state, Color.WHITE)
    assert validate_move(source, Square(2, 2), game_state, Color.WHITE)
    assert validate_move(source, Square(1, 1), game_state, Color.WHITE)
    assert validate_move(source, Square(0, 0), game_state, Color.WHITE)
    assert validate_move(source, Square(2, 4), game_state, Color.WHITE)
    assert validate_move(source, Square(1, 5), game_state, Color.WHITE)
    assert validate_move(source, Square(0, 6), game_state, Color.WHITE)
    assert validate_move(source, Square(4, 4), game_state, Color.WHITE)
    assert validate_move(source, Square(5, 5), game_state, Color.WHITE)
    assert validate_move(source, Square(6, 6), game_state, Color.WHITE)
    assert validate_move(source, Square(7, 7), game_state, Color.WHITE)

def test_queen_can_not_move_outside_of_board():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(3, 3)
    game_state.place_piece(Queen(Color.WHITE), source)
    assert not validate_move(source, Square(3, 8), game_state, Color.WHITE)
    assert not validate_move(source, Square(-1, 3), game_state, Color.WHITE)
    assert not validate_move(source, Square(8, 3), game_state, Color.WHITE)
    assert not validate_move(source, Square(3, -1), game_state, Color.WHITE)
    assert not validate_move(source, Square(8, 8), game_state, Color.WHITE)
    assert not validate_move(source, Square(8, -1), game_state, Color.WHITE)
    assert not validate_move(source, Square(-1, -1), game_state, Color.WHITE)
    assert not validate_move(source, Square(-1, 8), game_state, Color.WHITE)

def test_some_blind_spots_of_queen():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(3, 3)
    game_state.place_piece(Queen(Color.WHITE), source)
    assert not validate_move(source, Square(5, 4), game_state, Color.WHITE)
    assert not validate_move(source, Square(7, 0), game_state, Color.WHITE)
    assert not validate_move(source, Square(4, 1), game_state, Color.WHITE)
    assert not validate_move(source, Square(2, 5), game_state, Color.WHITE)

# King test cases
def test_king_can_move_one_square_straight():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(3, 3)
    game_state.place_piece(King(Color.WHITE), source)
    assert validate_move(source, Square(3, 4), game_state, Color.WHITE)
    assert validate_move(source, Square(4, 3), game_state, Color.WHITE)
    assert validate_move(source, Square(3, 2), game_state, Color.WHITE)
    assert validate_move(source, Square(2, 3), game_state, Color.WHITE)

def test_king_can_move_one_square_diagonal():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(3, 3)
    game_state.place_piece(King(Color.WHITE), source)
    assert validate_move(source, Square(4, 4), game_state, Color.WHITE)
    assert validate_move(source, Square(4, 2), game_state, Color.WHITE)
    assert validate_move(source, Square(2, 2), game_state, Color.WHITE)
    assert validate_move(source, Square(2, 4), game_state, Color.WHITE)

def test_king_can_only_move_one_square():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(3, 3)
    game_state.place_piece(King(Color.WHITE), source)
    assert not validate_move(source, Square(5, 1), game_state, Color.WHITE)
    assert not validate_move(source, Square(6, 0), game_state, Color.WHITE)
    assert not validate_move(source, Square(1, 1), game_state, Color.WHITE)
    assert not validate_move(source, Square(0, 0), game_state, Color.WHITE)
    assert not validate_move(source, Square(1, 5), game_state, Color.WHITE)
    assert not validate_move(source, Square(0, 6), game_state, Color.WHITE)
    assert not validate_move(source, Square(5, 5), game_state, Color.WHITE)
    assert not validate_move(source, Square(6, 6), game_state, Color.WHITE)
    assert not validate_move(source, Square(7, 7), game_state, Color.WHITE)
    assert not validate_move(source, Square(3, 5), game_state, Color.WHITE)
    assert not validate_move(source, Square(3, 6), game_state, Color.WHITE)
    assert not validate_move(source, Square(3, 7), game_state, Color.WHITE)
    assert not validate_move(source, Square(1, 3), game_state, Color.WHITE)
    assert not validate_move(source, Square(0, 3), game_state, Color.WHITE)
    assert not validate_move(source, Square(5, 3), game_state, Color.WHITE)
    assert not validate_move(source, Square(6, 3), game_state, Color.WHITE)
    assert not validate_move(source, Square(7, 3), game_state, Color.WHITE)
    assert not validate_move(source, Square(3, 1), game_state, Color.WHITE)
    assert not validate_move(source, Square(3, 0), game_state, Color.WHITE)

def test_king_can_not_move_outside_board():
    game_state = GameStateFactory.create_empty_game_state()
    source = Square(7, 7)
    game_state.place_piece(King(Color.WHITE), source)
    assert not validate_move(source, Square(8, 8), game_state, Color.WHITE)
    assert not validate_move(source, Square(8, 7), game_state, Color.WHITE)
    assert not validate_move(source, Square(7, 8), game_state, Color.WHITE)
    assert not validate_move(source, Square(8, 6), game_state, Color.WHITE)
    assert not validate_move(source, Square(6, 8), game_state, Color.WHITE)