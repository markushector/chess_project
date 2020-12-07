class Piece():
    def __init__(self, start_pos, type, color):
        self.position = start_pos
        self.type = type
        self.color

    def move(self, new_pos):
        if self._legal_move(new_pos)
            self.position = new_pos

    def _legal_move(self):
        pass


class Pawn(Piece):
    def __init__(self, start_pos, type, color):
        super(Pawn, self).__init__(start_pos, type)

    def _legal_move(self, new_pos):
        if self.color:
            if self.position[0] - new_pos[0] == -1 and self.position[1] == new_pos[1]:
                return True
        else:
            if self.position[0] - new_pos[0] == 1 and self.position[1] == new_pos[1]:
                return True

        return False


    def _legal_capture(self, capture_pos):
        diagonal
        if self.color:
            if self.position[0] - new_pos[0] == -1 and self.position[1] == new_pos[1]:
                return True
        else:
            if self.position[0] - new_pos[0] == 1 and self.position[1] == new_pos[1]:
                return True


class Knight(Piece):
    def __init__(self, start_pos, type, color):
        super(Pawn, self).__init__(start_pos, type)

    def _legal_move(self, new_pos):
        if abs(self.position[0]-new_pos[0]) == 1 and abs(self.position[1]-new_pos[1]) == 2:
            return True
        elif abs(self.position[0]-new_pos[0]) == 2 and abs(self.position[1]-new_pos[1]) == 1:
            return True
        else:
            return False


class Bishop(Piece):
    def __init__(self, start_pos, type, color):
        super(Pawn, self).__init__(start_pos, type)

    def _legal_move(self, new_pos):
        if abs(self.position[0]-new_pos[0]) == abs(self.position[1]-new_pos[1]):
            return True
        else:
            return False


class Rook(Piece):
    def __init__(self, start_pos, type, color):
        super(Pawn, self).__init__(start_pos, type)

    def _legal_move(self, new_pos):
        if self.position[0] != new_pos[0] and self.position[1] == new_pos[1]:
            return True
        elif self.position[0] == new_pos[0] and self.position[1] != new_pos[1]:
            return True
        else:
            return False


class King(Piece):
    def __init__(self, start_pos, type, color):
        super(Pawn, self).__init__(start_pos, type)

    def _legal_move(self, new_pos):
        if self.color:
            if self.position[0] - new_pos[0] == -1 and self.position[1] == new_pos[1]:
                return True
        else:
            if self.position[0] - new_pos[0] == 1 and self.position[1] == new_pos[1]:
                return True

        return False


class Queen(Piece):
    def __init__(self, start_pos, type, color):
        super(Pawn, self).__init__(start_pos, type)
        self.is_promoted_pawn = False

    def _legal_move(self, new_pos):
        if self.position[0] != new_pos[0] and self.position[1] == new_pos[1]:
            return True
        elif self.position[0] == new_pos[0] and self.position[1] != new_pos[1]:
            return True
        elif abs(self.position[0]-new_pos[0]) == abs(self.position[1]-new_pos[1]):
            return True
        else:
            return False


class ChessBoard():

    WHITE_PAWN_LIST = [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)]
    WHITE_BISHOP_LIST = [(0, 2), (0, 5)]
    WHITE_KNIGHT_LIST = [(0, 1), (0, 6)]
    WHITE_ROOK_LIST = [(0, 0), (0, 7)]
    WHITE_QUEEN = (0, 3)
    WHITE_KING = (0, 4)

    BLACK_PAWN_LIST = [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)]
    BLACK_BISHOP_LIST = [(7, 2), (7, 5)]
    BLACK_KNIGHT_LIST = [(7, 1), (7, 6)]
    BLACK_ROOK_LIST = [(7, 0), (7, 7)]
    BLACK_QUEEN = (7, 3)
    BLACK_KING = (7, 4)

    def __init__(self):
        self.board = self._init_board()

    def _init_board(self):
        board = []
        for i in range(8):
            row = []
            for j in range(8):
                piece = _get_piece((i, j))
                row.append(piece)
            board.append(row)
        return board

    def _get_piece(self, square):
        if square in self.WHITE_PAWN_LIST:
            piece = Pawn(square, "pawn", True)
        elif square in self.WHITE_KNIGHT_LIST:
            piece = Knight(square, "knight", True)
        elif square in self.WHITE_BISHOP_LIST:
            piece = Bishop(square, "bishop", True)
        elif square in self.WHITE_ROOK_LIST:
            piece = Rook(square, "rook", True)
        elif square == self.WHITE_QUEEN:
            piece = Queen(square, "queen", True)
        elif square == self.WHITE_KING:
            piece = King(square, "king", True)

        elif square in self.BLACK_PAWN_LIST:
            piece = Pawn(square, "pawn", False)
        elif square in self.BLACK_KNIGHT_LIST:
            piece = Knight(square, "knight", False)
        elif square in self.BLACK_BISHOP_LIST:
            piece = Bishop(square, "bishop", False)
        elif square in self.BLACK_ROOK_LIST:
            piece = Rook(square, "rook", False)
        elif square == self.BLACK_QUEEN:
            piece = Queen(square, "queen", False)
        elif square == self.BLACK_KING:
            piece = King(square, "king", False)

    def _update_board(self, square, new_square):
        piece = self.board[square]
        self.board[square] = None
        self.board[new_square] = piece
