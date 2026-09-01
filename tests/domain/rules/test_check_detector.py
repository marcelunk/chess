from chess.domain.color import Color
from chess.domain.game_state import GameStateFactory
from chess.domain.moves.move_validator import validate_move
from chess.domain.pieces.bishop import Bishop
from chess.domain.pieces.king import King
from chess.domain.pieces.pawn import Pawn
from chess.domain.pieces.queen import Queen
from chess.domain.rules.check_detector import game_state_is_in_check
from chess.domain.square import Square


def test_white_king_in_check():
    game_state = GameStateFactory.create_empty_game_state()
    game_state.place_piece(King(Color.WHITE), Square.from_string('e1'), False)
    game_state.place_piece(Bishop(Color.BLACK), Square.from_string('a5'), False)
    assert game_state_is_in_check(game_state, Color.WHITE)


def test_black_king_in_check():
    game_state = GameStateFactory.create_empty_game_state()
    game_state.place_piece(King(Color.BLACK), Square.from_string('e8'), False)
    game_state.place_piece(Queen(Color.WHITE), Square.from_string('e3'), False)
    assert game_state_is_in_check(game_state, Color.BLACK)

def test_figure_pinned_due_to_check():
    game_state = GameStateFactory.create_empty_game_state()
    game_state.place_piece(King(Color.WHITE), Square.from_string('e1'), True)
    game_state.place_piece(Pawn(Color.WHITE), Square.from_string('d2'), True)
    game_state.place_piece(Queen(Color.BLACK), Square.from_string('b4'), False)
    is_valid = validate_move(Square.from_string('d2'), Square.from_string('d3'), game_state, Color.WHITE)
    assert not is_valid

def test_king_is_threaten_by_knight():
    pass

def test_check_due_to_en_passant():
    pass