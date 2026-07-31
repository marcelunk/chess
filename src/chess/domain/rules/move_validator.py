from chess.domain.color import Color
from chess.domain.game_state import GameState
from chess.domain.pieces.pawn import Pawn
from chess.domain.square import Square


class MoveValidator:

    @staticmethod
    def validate_move(source: Square, target: Square, game_state: GameState, turn: Color) -> bool:
        if not MoveValidator._is_inside_board(target):
            return False

        piece = game_state.get_piece(source)
        if piece == None or piece.color != turn:
            return False

        legal_moves = MoveValidator._get_legal_moves(source, game_state, piece)
        return target in legal_moves

    @staticmethod
    def _get_legal_moves(source, game_state, piece):
        legal_moves = set()
        color = piece.color

        legal_moves = legal_moves.union(MoveValidator._get_possible_moves(source.file, source.rank, game_state, piece, color))

        if isinstance(piece, Pawn):
            legal_moves = legal_moves.union(MoveValidator._get_pawn_edge_cases(source, game_state, piece, color))

        # TODO add rochade

        return legal_moves

    @staticmethod
    def _get_possible_moves(file, rank, game_state, piece, color):
        legal_moves = set()
        for pattern in piece.move_patterns:
            vector = pattern.direction
            max_distance = pattern.max_distance
            for i in range(1, max_distance + 1):
                diff_file = i * vector[0]
                diff_rank = i * vector[1]
                square = Square(file + diff_file, rank + diff_rank)
                if not MoveValidator._is_inside_board(square):
                    break

                p = game_state.get_piece(square)
                if p != None and p.color == color:
                    break
                elif p != None and p.color != color:
                    legal_moves.add(square)
                    break

                legal_moves.add(square)

        return legal_moves

    @staticmethod
    def _get_pawn_edge_cases(source, game_state, piece, color):
        file = source.file
        rank = source.rank
        legal_moves = set()

        if piece.in_start_position:
            legal_moves.add(Square(file, rank + 2))

        s_1 = Square(file + 1, rank + 1)
        if MoveValidator._is_inside_board(s_1):
            x = game_state.get_piece(s_1)
            if x != None and x.color != color:
                legal_moves.add(s_1)

        s_2 = Square(file - 1, rank + 1)
        if MoveValidator._is_inside_board(s_2):
            y = game_state.get_piece(s_2)
            if y != None and y.color != color:
                legal_moves.add(s_2)

        # TODO add en passant

        # TODO add change piece

        return legal_moves

    @staticmethod
    def _is_inside_board(square):
        return (square.file >= 0 and square.file < 8) and (square.rank >= 0 and square.rank < 8)