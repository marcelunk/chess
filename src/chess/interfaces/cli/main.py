from chess.application.game_service import GameService
from chess.interfaces.cli.cli import CLI


def main() -> None:
    service = GameService()
    cli = CLI(service)
    cli.run()

if __name__ == "__main__":
    main()