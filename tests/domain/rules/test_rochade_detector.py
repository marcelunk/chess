from chess.domain.color import Color
from chess.domain.game_state import GameStateFactory
from chess.domain.pieces.bishop import Bishop
from chess.domain.pieces.king import King
from chess.domain.pieces.pawn import Pawn
from chess.domain.pieces.rook import Rook
from chess.domain.rules.rochade_detector import long_rochade_is_possible, short_rochade_is_possible
from chess.domain.square import Square


def test_rochade_is_possible():
    game_state = GameStateFactory.create_empty_game_state()
    game_state.place_piece(Rook(Color.WHITE), Square.from_string('a1'), True)
    game_state.place_piece(Rook(Color.WHITE), Square.from_string('h1'), True)
    game_state.place_piece(King(Color.WHITE), Square.from_string('e1'), True)
    assert long_rochade_is_possible(game_state, Color.WHITE)
    assert short_rochade_is_possible(game_state, Color.WHITE)

def test_king_already_moved():
    game_state = GameStateFactory.create_empty_game_state()
    game_state.place_piece(Rook(Color.WHITE), Square.from_string('h1'), True)
    game_state.place_piece(King(Color.WHITE), Square.from_string('e1'), True)
    game_state.make_move(Square.from_string('e1'), Square.from_string('d1'))
    game_state.make_move(Square.from_string('d1'), Square.from_string('e1'))
    assert not long_rochade_is_possible(game_state, Color.WHITE)
    assert not short_rochade_is_possible(game_state, Color.WHITE)

def test_rook_already_moved():
    game_state = GameStateFactory.create_empty_game_state()
    game_state.place_piece(Rook(Color.WHITE), Square.from_string('a1'), True)
    game_state.place_piece(Rook(Color.WHITE), Square.from_string('h1'), True)
    game_state.place_piece(King(Color.WHITE), Square.from_string('e1'), True)
    game_state.make_move(Square.from_string('h1'), Square.from_string('h3'))
    game_state.make_move(Square.from_string('h3'), Square.from_string('h1'))
    assert long_rochade_is_possible(game_state, Color.WHITE)
    assert not short_rochade_is_possible(game_state, Color.WHITE)

def test_king_is_blocked_by_same_color():
    game_state = GameStateFactory.create_empty_game_state()
    game_state.place_piece(Rook(Color.WHITE), Square.from_string('a1'), True)
    game_state.place_piece(Rook(Color.WHITE), Square.from_string('h1'), True)
    game_state.place_piece(King(Color.WHITE), Square.from_string('e1'), True)
    game_state.place_piece(Bishop(Color.WHITE), Square.from_string('c1'), True)
    assert not long_rochade_is_possible(game_state, Color.WHITE)
    assert short_rochade_is_possible(game_state, Color.WHITE)

def test_king_is_blocked_by_other_color():
    game_state = GameStateFactory.create_empty_game_state()
    game_state.place_piece(Rook(Color.WHITE), Square.from_string('a1'), True)
    game_state.place_piece(Rook(Color.WHITE), Square.from_string('h1'), True)
    game_state.place_piece(King(Color.WHITE), Square.from_string('e1'), True)
    game_state.place_piece(Bishop(Color.BLACK), Square.from_string('c1'), False)
    assert not long_rochade_is_possible(game_state, Color.WHITE)
    assert short_rochade_is_possible(game_state, Color.WHITE)

def test_king_is_in_check():
    game_state = GameStateFactory.create_empty_game_state()
    game_state.place_piece(Rook(Color.WHITE), Square.from_string('a1'), True)
    game_state.place_piece(Rook(Color.WHITE), Square.from_string('h1'), True)
    game_state.place_piece(King(Color.WHITE), Square.from_string('e1'), True)
    game_state.place_piece(Rook(Color.BLACK), Square.from_string('e6'), False)
    assert not long_rochade_is_possible(game_state, Color.WHITE)
    assert not short_rochade_is_possible(game_state, Color.WHITE)

def test_kings_way_is_in_check_short():
    game_state = GameStateFactory.create_empty_game_state()
    game_state.place_piece(Rook(Color.WHITE), Square.from_string('a1'), True)
    game_state.place_piece(Rook(Color.WHITE), Square.from_string('h1'), True)
    game_state.place_piece(King(Color.WHITE), Square.from_string('e1'), True)
    game_state.place_piece(Rook(Color.BLACK), Square.from_string('d6'), False)
    assert not long_rochade_is_possible(game_state, Color.WHITE)
    assert short_rochade_is_possible(game_state, Color.WHITE)

def test_kings_way_is_in_check_long():
    game_state = GameStateFactory.create_empty_game_state()
    game_state.place_piece(Rook(Color.WHITE), Square.from_string('a1'), True)
    game_state.place_piece(Rook(Color.WHITE), Square.from_string('h1'), True)
    game_state.place_piece(King(Color.WHITE), Square.from_string('e1'), True)
    game_state.place_piece(Rook(Color.BLACK), Square.from_string('f6'), False)
    assert long_rochade_is_possible(game_state, Color.WHITE)
    assert not short_rochade_is_possible(game_state, Color.WHITE)

def test_kings_target_is_in_check():
    game_state = GameStateFactory.create_empty_game_state()
    game_state.place_piece(Rook(Color.WHITE), Square.from_string('a1'), True)
    game_state.place_piece(Rook(Color.WHITE), Square.from_string('h1'), True)
    game_state.place_piece(King(Color.WHITE), Square.from_string('e1'), True)
    game_state.place_piece(Rook(Color.BLACK), Square.from_string('b6'), False)
    assert not long_rochade_is_possible(game_state, Color.WHITE)
    assert short_rochade_is_possible(game_state, Color.WHITE)