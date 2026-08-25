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
        return not self.is_light

    @property
    def is_inside_board(self) -> bool:
        return (self.file >= 0 and self.file < 8) and (self.rank >= 0 and self.rank < 8)

    @property
    def is_outside_board(self) -> bool:
        return not self.is_inside_board

    def __str__(self):
        return f"{chr(self.file + ord('a'))}{self.rank + 1}"