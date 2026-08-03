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

        legal_moves = legal_moves.union(MoveValidator._get_possible_moves(source.file, source.rank, game_state, piece))

        if isinstance(piece, Pawn):
            legal_moves = legal_moves.union(MoveValidator._get_pawn_edge_cases(source, game_state, piece))

        # TODO add rochade

        return legal_moves

    @staticmethod
    def _get_possible_moves(file, rank, game_state, piece):
        color = piece.color
        legal_moves = set()
        for pattern in piece.move_patterns:
            vector = pattern.direction
            max_distance = pattern.max_distance

            if isinstance(piece, Pawn) and piece.in_start_position:
                max_distance = 2

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
    def _get_pawn_edge_cases(source, game_state, pawn):
        color = pawn.color
        file = source.file
        rank = source.rank
        legal_moves = set()

        vector_left = None
        vector_right = None
        if color == Color.WHITE:
            vector_left = (-1, 1)
            vector_right = (1, 1)
        else:
            vector_left = (-1, -1)
            vector_right = (1, -1)

        left_diagonal = Square(file + vector_left[0], rank + vector_left[1])
        if MoveValidator._pawn_can_hit(game_state, color, left_diagonal):
            legal_moves.add(left_diagonal)

        right_diagonal = Square(file + vector_right[0], rank + vector_right[1])
        if MoveValidator._pawn_can_hit(game_state, color, right_diagonal):
            legal_moves.add(right_diagonal)



        en_passant_square = game_state.en_passant_square
        if MoveValidator._en_passant_is_allowed(en_passant_square, source):
            legal_moves.add(en_passant_square)

        # TODO add change piece

        return legal_moves

    @staticmethod
    def _pawn_can_hit(game_state, color, square):
        if not MoveValidator._is_inside_board(square):
            return False
        x = game_state.get_piece(square)
        return x != None and x.color != color

    @staticmethod
    def _en_passant_is_allowed(en_passant_square, source):
        if en_passant_square == None:
            return False
        
        one_file_difference = (en_passant_square.file - source.file) % 1 == 0
        return one_file_difference and en_passant_square.rank == source.rank

    @staticmethod
    def _is_inside_board(square):
        return (square.file >= 0 and square.file < 8) and (square.rank >= 0 and square.rank < 8)