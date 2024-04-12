

class FullColumn(Exception):
    pass

class MoveOutOfRange(Exception):
    pass


class Game:
    def __init__(self):
        self.round = 1
        self.turn = 'X'  # 'X' starts first
        self.moves = list()
        self.board = list()
        self.col_size = [0] * 7
        self.winner = None

        for i in range(6):
            self.board.append(['O'] * 7)

    def print_board(self):
        print("\n0 1 2 3 4 5 6")
        print("-- Columns --")
        for row in reversed(self.board):
            print(" ".join(row))
        print("")

    def is_valid_move(self, col):
        if not 0 <= col <= 6:
            raise MoveOutOfRange
        if self.col_size[col] == 6:
            raise FullColumn
        return True

    def move(self, col):
        """Put the current player's disc in the column 'col'"""
        # check if the game is already decided
        if self.winner:
            return

        # the following can raise exceptions
        self.is_valid_move(col)

        row = self.col_size[col]

        # moves is used to allow undoing a move
        self.moves.append(col)
        self.board[row][col] = self.turn
        self.col_size[col] += 1

        if self.check_for_win(row, col):
            self.winner = self.turn
            return

        # the are at most 42 moves, so if this is the 42 move,
        # yet there is no winner, the game is over
        if self.round >= 6 * 7:
            self.winner = 'D'

        self.switch_turn()

    def undo_move(self):
        if self.round <= 1:
            return
        # extract the last move
        col = self.moves.pop()
        # restore the column size
        self.col_size[col] -= 1
        # the row of last move
        row = self.col_size[col]

        # switch_turn switches the players, but also advances the round by 1
        # so in the next line we reduce it by 2
        self.switch_turn()
        self.round -= 2
        # delete the disc from the board
        self.board[row][col] = 'O'

    def check_for_win(self, row, col):
        # empty cell cannot be a winner...
        if self.board[row][col] == 'O':
            return False

        # check for all kinds of possilbe wins: vertical, horizontal or
        # diagonal
        return self.is_vertical_four(row, col) or self.is_horizontal_four(
            row, col) or self.is_diagonal_four(row, col)

    def is_vertical_four(self, row, col):
        """Check for vertical win"""
        count = 0
        player = self.board[row][col]
        for i in range(4):
            if i <= row and self.board[row - i][col] == player:
                count += 1

        if count == 4:
            return True

        return False

    def is_horizontal_four(self, row, col):
        """Check for horizontal win"""
        player = self.board[row][col]
        consecutiveL = 0
        consecutiveR = 0
        # count consecutive left discs
        i = col
        current = player
        while current == player:
            consecutiveL += 1
            i -= 1
            if i < 0:
                break
            current = self.board[row][i]

        # count consecutive right discs
        i = col
        current = self.board[row][i]
        while current == player:
            consecutiveR += 1
            i += 1
            if i >= 7:
                break
            current = self.board[row][i]

        # since (row, col) cell was counted twice, we reduce by 1
        if consecutiveL + consecutiveR - 1 >= 4:
            return True

        return False

    def is_diagonal_four(self, row, col):
        """Check for diagonal win"""
        return self.is_neg_diagonal_four(
            row, col) or self.is_pos_diagonal_four(row, col)

    def is_neg_diagonal_four(self, row, col):
        """Check for negative slope diagonal"""
        player = self.board[row][col]
        consecutive = 0

        i = row
        j = col
        current = player
        while current == player:
            consecutive += 1
            i -= 1
            j += 1
            if i < 0 or j >= 7:
                break
            current = self.board[i][j]

        i = row
        j = col
        current = player
        while current == player:
            consecutive += 1
            i += 1
            j -= 1
            if i >= 6 or j < 0:
                break
            current = self.board[i][j]

        if consecutive - 1 >= 4:
            return True
        return False

    def is_pos_diagonal_four(self, row, col):
        """Check for positive slope diagonal"""
        player = self.board[row][col]
        consecutive = 0

        current = player
        i = row
        j = col
        while current == player:
            consecutive += 1
            i -= 1
            j -= 1
            if i < 0 or j < 0:
                break
            current = self.board[i][j]

        current = player
        i = row
        j = col
        while current == player:
            consecutive += 1
            i += 1
            j += 1
            if i >= 6 or j >= 7:
                break
            current = self.board[i][j]

        if consecutive - 1 >= 4:
            return True
        return False

    def switch_turn(self):
        self.round += 1
        self.turn = 'X' if self.turn == 'Y' else 'Y'

    def get_winning_discs(self):
        """
        Return a list of (row, col) tuples representing
        each of the winning discs
        """
        for i in range(6):
            for j in range(7):
                if self.board[i][j] == 'O':
                    continue
                if self.is_horizontal_four(i, j):
                    return [(i, x) for x in range(j, j + 4)]
                if self.is_vertical_four(i, j):
                    return [(x, j) for x in range(i, i - 4, -1)]
                if self.is_neg_diagonal_four(i, j):
                    return [(x, y) for x, y in zip(
                        range(i, i + 4), range(j, j - 4, -1))]
                if self.is_pos_diagonal_four(i, j):
                    return [(x, y)
                            for x, y in zip(range(i, i + 4), range(j, j + 4))]