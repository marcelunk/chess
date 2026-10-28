import re

from chess.domain.color import Color
from chess.domain.game import Game
from chess.domain.square import Square

class GameService:

    def __init__(self) -> None:
        self.input_pattern = re.compile('^[a-h][1-8][a-h][1-8]$')
        self._game: Game | None = None

    def new_game(self) -> None:
        self._game = Game()

    def print_game_state(self) -> None:
        self._game.print_game_state()

    def make_move(self, input: str) -> None:
        game = self._require_game()
        self._validate_input(input)
        source = input[0:2]
        target = input[2:4]
        game.make_move(Square.from_string(source), Square.from_string(target))


    def undo(self) -> None:
        pass

    def redo(self) -> None:
        pass

    def turn(self) -> Color:
        game = self._require_game()
        return game.turn

    def _require_game(self) -> Game:
        if self._game is None:
            raise RuntimeError('No active game')

        return self._game

    def _validate_input(self, input):
        if self.input_pattern.match(input) is None:
            raise RuntimeError(f"Invalid input: {input}")