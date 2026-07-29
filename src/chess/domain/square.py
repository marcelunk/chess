from dataclasses import dataclass

@dataclass(frozen=True, order=True)
class Square:
    file: int   # column 0-7
    rank: int   # row 0-7

    @classmethod
    def from_string(cls, text: str):
        return cls(ord(text[0]) - ord('a'), int(text[1]) - 1)

    @property
    def is_light(self) -> bool:
        return (self.file + self.rank) % 2 == 1

    @property
    def is_dark(self) -> bool:
        return (self.file + self.rank) % 2 == 0

    def __str__(self):
        return f"{chr(self.file + ord('a'))}{self.rank + 1}"

    def __eq__(self, value):
        if isinstance(value, Square):
            return self.file == value.file and self.rank == value.rank
        else:
            return False

    def __hash__(self):
        return hash(str(self.file) + str(self.rank))
