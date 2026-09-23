from chess.domain.color import Color
from chess.domain.game_state import GameStateFactory
from chess.domain.pieces.bishop import Bishop
from chess.domain.pieces.king import King
from chess.domain.pieces.knight import Knight
from chess.domain.pieces.pawn import Pawn
from chess.domain.pieces.queen import Queen
from chess.domain.pieces.rook import Rook
from chess.domain.rules.checkmate_detector import game_state_is_in_checkmate
from chess.domain.square import Square


def test_attacker_can_be_captured():
    game_state = GameStateFactory.create_empty_game_state()
    game_state.place_piece(King(Color.WHITE), Square.from_string('e1'), False)
    game_state.place_piece(Rook(Color.WHITE), Square.from_string('d1'), False)
    game_state.place_piece(Pawn(Color.WHITE), Square.from_string('d2'), False)
    game_state.place_piece(Rook(Color.WHITE), Square.from_string('f1'), False)
    game_state.place_piece(Pawn(Color.WHITE), Square.from_string('f2'), False)
    game_state.place_piece(Knight(Color.WHITE), Square.from_string('c5'), False)
    game_state.place_piece(Rook(Color.BLACK), Square.from_string('e4'), False)
    assert not game_state_is_in_checkmate(game_state, Color.WHITE)

def test_attacker_can_be_blocked():
    pass

def test_king_can_move_away():
    pass

def test_checkmate():
    pass

def test_checkmate_by_knight():
    pass