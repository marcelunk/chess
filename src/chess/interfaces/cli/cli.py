import re

from chess.application.game_service import GameService


class CLI:

    def __init__(self, service: GameService):
        self._service = service
        self._legal_move_format = re.compile('^(\\w\\d){2}$')
        self._legal_commands = {'quit', 'help', 'undo', 'redo'}

    def run(self):
        self._service.new_game()
        while True:
            self._service.print_game_state()

            command = input("> ")
            sanitized = command.lower()

            match = self._legal_move_format.match(sanitized)
            is_command = sanitized in self._legal_commands
            is_move = match is not None

            if not is_command and not is_move:
                print('Illegal input')
                print()
                continue

            if is_command:
                if command == 'quit':
                    break
                elif command == 'help':
                    print('Print help')
                elif command == 'redo':
                    self._service.redo()
                elif command == 'undo':
                    self._service.undo()

            if is_move:
                self._service.make_move(sanitized)