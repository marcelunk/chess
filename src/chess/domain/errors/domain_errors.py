class InvalidMoveError(ValueError):

    def __init__(self, *args, move: str):
        super().__init__(*args)
        self.move = move