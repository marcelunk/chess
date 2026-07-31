import re
from chess.domain.color import Color
from chess.domain.game_state import GameStateFactory
from chess.domain.rules.move_validator import MoveValidator
from chess.domain.square import Square

class Game:

    def __init__(self):
        self.input_pattern = re.compile('^[a-h][1-8]$')
        self.history = list()
        self._current_game_state = GameStateFactory.create_initial_game_state()
        self._turn = Color.White

    def print_game_state(self):
        print(str(self._current_game_state))

    def make_move(self, source: str, target: str):
        self._validate_input(source)
        self._validate_input(target)
        # validate move
        source_square = Square.from_string(source)
        target_square = Square.from_string(target)
        is_valid = MoveValidator.validate_move(source_square, target_square, self._current_game_state, self._turn)
        if is_valid:
            # make move
            self.history.append(self._current_game_state)
            self._current_game_state = self._current_game_state.make_move(source_square, target_square)
            if self._turn == Color.WHITE:
                self._turn = Color.BLACK
            else:
                self._turn = Color.WHITE

    def get_piece(self, square: str):
        self._validate_input(square)
        square = Square.from_string(square)
        return self._current_game_state.get_piece(square)

    def _validate_input(self, input):
        if self.input_pattern.match(input) == None:
            raise RuntimeError("Bad input: {input}")