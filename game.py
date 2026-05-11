import random


class DaraGame:
    def __init__(self):
        self.rows = 5
        self.cols = 6

        self.board = [["." for _ in range(self.cols)] for _ in range(self.rows)]

        self.current_player = random.choice(["X", "O"])

        self.phase = "placement"

        self.pieces = {
            "X": 0,
            "O": 0
        }

        self.chat_messages = []

        self.winner = None

    # =========================
    # STATUS DO JOGO
    # =========================
    def get_state(self):
        return {
            "board": self.board,
            "current_player": self.current_player,
            "phase": self.phase,
            "winner": self.winner,
            "chat": self.chat_messages[-20:]
        }

    # =========================
    # TROCAR JOGADOR
    # =========================
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    # =========================
    # CHAT
    # =========================
    def send_chat(self, player, message):
        self.chat_messages.append(f"{player}: {message}")
        return True

    # =========================
    # FASE DE COLOCAÇÃO
    # =========================
    def place_piece(self, player, row, col):

        if player != self.current_player:
            return False

        if self.board[row][col] != ".":
            return False

        self.board[row][col] = player

        # NÃO pode formar 3 nessa fase
        if self.check_three(row, col):
            self.board[row][col] = "."
            return False

        self.pieces[player] += 1

        # muda de fase
        if self.pieces["X"] == 12 and self.pieces["O"] == 12:
            self.phase = "movement"

        self.switch_player()

        return True

    # =========================
    # MOVIMENTO
    # =========================
    def move_piece(self, player, fr, fc, tr, tc):

        if player != self.current_player:
            return False

        if self.board[fr][fc] != player:
            return False

        if self.board[tr][tc] != ".":
            return False

        # adjacente
        if abs(fr - tr) + abs(fc - tc) != 1:
            return False

        self.board[fr][fc] = "."
        self.board[tr][tc] = player

        # captura
        if self.check_three(tr, tc):
            return "REMOVE"

        self.switch_player()

        return True

    # =========================
    # REMOVER PEÇA
    # =========================
    def remove_piece(self, player, row, col):

        opponent = "O" if player == "X" else "X"

        if self.board[row][col] != opponent:
            return False

        self.board[row][col] = "."

        self.pieces[opponent] -= 1

        # verifica vencedor
        if self.pieces[opponent] < 3:
            self.winner = player

        self.switch_player()

        return True

    # =========================
    # VERIFICAR 3 EM LINHA
    # =========================
    def check_three(self, row, col):

        player = self.board[row][col]

        # horizontal
        count = 0

        for c in range(self.cols):

            if self.board[row][c] == player:
                count += 1

                if count == 3:
                    return True

            else:
                count = 0

        # vertical
        count = 0

        for r in range(self.rows):

            if self.board[r][col] == player:
                count += 1

                if count == 3:
                    return True

            else:
                count = 0

        return False

    # =========================
    # DESISTIR
    # =========================
    def quit_game(self, player):

        self.winner = "O" if player == "X" else "X"

        return True