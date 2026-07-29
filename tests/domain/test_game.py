from chess.domain.game import Game
from chess.domain.pieces.pawn import Pawn


def test_game_make_move():
    game = Game()
    source = "a2"
    target = "a3"
    pawn_1 = game.get_piece(source)
    no_piece_1 = game.get_piece(target)

    assert isinstance(pawn_1, Pawn)
    assert no_piece_1 == None

    game.make_move(source, target)

    pawn_2 = game.get_piece(target)
    no_piece_2 = game.get_piece(source)

    assert isinstance(pawn_2, Pawn)
    assert pawn_1 == pawn_2
    assert no_piece_2 == None

def test_piece_toggles_start_position_after_move():
    game = Game()
    source = "a2"
    target = "a3"
    pawn = game.get_piece(source)

    assert pawn.in_start_position

    game.make_move(source, target)

    assert not pawn.in_start_position