import re
from chess.domain.color import Color
from chess.domain.game_state import GameStateFactory
from chess.domain.rules.check_detector import game_state_is_in_check
from chess.domain.rules.move_validator import validate_move
from chess.domain.square import Square

class Game:

    def __init__(self):
        self.input_pattern = re.compile('^[a-h][1-8][a-h][1-8]$')
        self.history = list()
        self.current_game_state = GameStateFactory.create_initial_game_state()

    def print_game_state(self):
        print(str(self.current_game_state))

    def make_move(self, input: str):
        self._validate_input(input)
        source = input[0:2]
        target = input[2:4]
        # validate move
        source_square = Square.from_string(source)
        target_square = Square.from_string(target)
        is_valid = validate_move(source_square, target_square, self.current_game_state, self.turn)
        if is_valid:
            # make move
            self.history.append(self.current_game_state)
            self.current_game_state = self.current_game_state.make_move(source_square, target_square)
            if game_state_is_in_check(self.current_game_state, self.turn):
                # rollback
                pass

    @property
    def turn(self) -> Color:
        if len(self.history) % 2 == 0:
            return Color.WHITE
        else:
            return Color.BLACK

    def _validate_input(self, input):
        if self.input_pattern.match(input) is None:
            raise RuntimeError(f"Bad input: {input}")