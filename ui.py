import tkinter as tk

ROWS = 5
COLS = 6

class DaraUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dara Game")

        self.buttons = []

        frame = tk.Frame(root)
        frame.pack()

        for r in range(ROWS):
            row = []
            for c in range(COLS):
                btn = tk.Button(frame, text=".", width=4, height=2,
                                command=lambda r=r, c=c: self.on_click(r, c))
                btn.grid(row=r, column=c)
                row.append(btn)
            self.buttons.append(row)

        self.status = tk.Label(root, text="Status")
        self.status.pack()

    def on_click(self, row, col):
        print(f"Clicou em {row}, {col}")

    def update_board(self, board):
        for r in range(ROWS):
            for c in range(COLS):
                self.buttons[r][c]["text"] = board[r][c]