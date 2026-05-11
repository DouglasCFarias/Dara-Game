import tkinter as tk
from tkinter import messagebox
from xmlrpc.client import ServerProxy

# =========================
# CONEXÃO RPC
# =========================
proxy = ServerProxy("http://localhost:8000/", allow_none=True)

PLAYER = "O"

ROWS = 5
COLS = 6


class DaraClient:

    def __init__(self, root):

        self.root = root
        self.root.title("Dara - Jogador O")

        self.selected = None
        self.awaiting_remove = False

        # =========================
        # TABULEIRO
        # =========================
        frame = tk.Frame(root)
        frame.pack()

        self.buttons = []

        for r in range(ROWS):

            row = []

            for c in range(COLS):

                btn = tk.Button(
                    frame,
                    text=".",
                    width=4,
                    height=2,
                    font=("Arial", 16),
                    command=lambda r=r, c=c: self.click(r, c)
                )

                btn.grid(row=r, column=c)

                row.append(btn)

            self.buttons.append(row)

        # =========================
        # STATUS
        # =========================
        self.status = tk.Label(
            root,
            text="Conectando...",
            font=("Arial", 12)
        )

        self.status.pack()

        # =========================
        # CHAT
        # =========================
        self.chat_box = tk.Text(
            root,
            height=10,
            width=50,
            state="disabled"
        )

        self.chat_box.pack()

        self.chat_entry = tk.Entry(root, width=40)
        self.chat_entry.pack()

        tk.Button(
            root,
            text="Enviar",
            command=self.send_chat
        ).pack()

        # =========================
        # DESISTIR
        # =========================
        tk.Button(
            root,
            text="Desistir",
            fg="red",
            command=self.quit_game
        ).pack()

        # =========================
        # UPDATE LOOP
        # =========================
        self.update_board()

    # =========================
    # UPDATE
    # =========================
    def update_board(self):

        state = proxy.get_state()

        board = state["board"]

        current_player = state["current_player"]

        phase = state["phase"]

        winner = state["winner"]

        chat = state["chat"]

        # =========================
        # TABULEIRO
        # =========================
        for r in range(ROWS):

            for c in range(COLS):

                value = board[r][c]

                self.buttons[r][c]["text"] = value

                if value == "X":
                    self.buttons[r][c]["bg"] = "lightcoral"

                elif value == "O":
                    self.buttons[r][c]["bg"] = "lightblue"

                else:
                    self.buttons[r][c]["bg"] = "white"

        # =========================
        # STATUS
        # =========================
        self.status["text"] = (
            f"Jogador atual: {current_player} | "
            f"Fase: {phase}"
        )

        # =========================
        # CHAT
        # =========================
        self.chat_box.config(state="normal")

        self.chat_box.delete(1.0, tk.END)

        for msg in chat:
            self.chat_box.insert(tk.END, msg + "\n")

        self.chat_box.config(state="disabled")

        # =========================
        # VENCEDOR
        # =========================
        if winner:
            messagebox.showinfo(
                "Fim de jogo",
                f"Jogador {winner} venceu!"
            )

            return

        # loop automático
        self.root.after(500, self.update_board)

    # =========================
    # CLIQUE
    # =========================
    def click(self, row, col):

        state = proxy.get_state()

        current_player = state["current_player"]

        phase = state["phase"]

        # NÃO é sua vez
        if current_player != PLAYER:
            return

        # =========================
        # REMOVER
        # =========================
        if self.awaiting_remove:

            result = proxy.remove_piece(
                PLAYER,
                row,
                col
            )

            if result:
                self.awaiting_remove = False

            return

        # =========================
        # PLACEMENT
        # =========================
        if phase == "placement":

            proxy.place_piece(
                PLAYER,
                row,
                col
            )

        # =========================
        # MOVEMENT
        # =========================
        else:

            if self.selected is None:

                self.selected = (row, col)

                self.status["text"] = (
                    f"Selecionado: {row}, {col}"
                )

            else:

                fr, fc = self.selected

                result = proxy.move_piece(
                    PLAYER,
                    fr,
                    fc,
                    row,
                    col
                )

                self.selected = None

                if result == "REMOVE":
                    self.awaiting_remove = True

    # =========================
    # CHAT
    # =========================
    def send_chat(self):

        message = self.chat_entry.get()

        if message:

            proxy.send_chat(
                PLAYER,
                message
            )

            self.chat_entry.delete(0, tk.END)

    # =========================
    # DESISTIR
    # =========================
    def quit_game(self):

        proxy.quit_game(PLAYER)


# =========================
# MAIN
# =========================
root = tk.Tk()

app = DaraClient(root)

root.mainloop()