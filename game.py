import random

class DaraGame:
    def __init__(self):
        self.rows = 5
        self.cols = 6
        self.board = [["." for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_player = random.choice(["X", "O"])
        self.phase = "placement"
        self.pieces = {"X": 0, "O": 0}

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def finalize_turn(self):
        self.switch_player()

    def place_piece(self, row, col):
        if self.board[row][col] != ".":
            return False

        self.board[row][col] = self.current_player

        if self.check_three_in_a_row(row, col):
            self.board[row][col] = "."
            return False

        self.pieces[self.current_player] += 1

        if self.pieces["X"] == 12 and self.pieces["O"] == 12:
            self.phase = "movement"

        self.switch_player()
        return True

    def check_three_in_a_row(self, row, col):
        player = self.board[row][col]

        count = 0
        for c in range(self.cols):
            if self.board[row][c] == player:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0

        count = 0
        for r in range(self.rows):
            if self.board[r][col] == player:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0

        return False

    def move_piece(self, fr, fc, tr, tc):
        if self.board[fr][fc] != self.current_player:
            return False

        if self.board[tr][tc] != ".":
            return False

        if abs(fr - tr) + abs(fc - tc) != 1:
            return False

        self.board[fr][fc] = "."
        self.board[tr][tc] = self.current_player

        if self.check_three_in_a_row(tr, tc):
            return "REMOVE"

        return True

    def remove_opponent_piece(self, row, col):
        opponent = "O" if self.current_player == "X" else "X"

        if self.board[row][col] == opponent:
            self.board[row][col] = "."
            self.pieces[opponent] -= 1
            return True

        return False

    def check_winner(self):
        if self.phase != "movement":
            return None

        if self.pieces["X"] < 3:
            return "O"
        if self.pieces["O"] < 3:
            return "X"

        return None