from chess.domain.color import Color
from chess.domain.game_state import GameStateFactory
from chess.domain.moves.move_validator import validate_move
from chess.domain.rules.checkmate_detector import is_checkmate
from chess.domain.rules.stalemate_detector import is_stalemate
from chess.domain.square import Square

class Game:

    def __init__(self):
        self.history = list()
        self.current_game_state = GameStateFactory.create_initial_game_state()

    def print_game_state(self):
        print(str(self.current_game_state))

    def make_move(self, source_square: Square, target_square: Square):
        valid = validate_move(source_square, target_square, self.current_game_state, self.turn)
        if not valid:
            raise RuntimeError('Invalid move according to current game state')

        # make move
        self.history.append(self.current_game_state)
        self.current_game_state = self.current_game_state.make_move(source_square, target_square)
        if is_checkmate(self.current_game_state, self.turn) or is_stalemate(self.current_game_state, self.turn):
            self.end_game()

    def undo_last_move(self):
        self.current_game_state = self.history.pop()

    def end_game(self):
        # TODO
        # Stop game loop
        # print and log game finished
        pass

    @property
    def turn(self) -> Color:
        return Color.WHITE if len(self.history) % 2 == 0 else Color.BLACK