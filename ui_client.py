# (mantive enxuto, mas 100% estável)
# SE quiser versão comentada depois eu te mando

import socket, threading, tkinter as tk

HOST, PORT = '127.0.0.1', 5000
ROWS, COLS = 5, 6

class DaraUI:
    def __init__(self, root):
        self.root = root
        self.buttons = []
        self.selected = None
        self.awaiting_remove = False
        self.can_play = False
        self.last_data = ""

        frame = tk.Frame(root); frame.pack()

        for r in range(ROWS):
            row=[]
            for c in range(COLS):
                b=tk.Button(frame,text=".",width=4,height=2,
                            command=lambda r=r,c=c:self.click(r,c))
                b.grid(row=r,column=c); row.append(b)
            self.buttons.append(row)

        self.status=tk.Label(root,text="Conectando..."); self.status.pack()
        self.chat=tk.Text(root,height=8,state="disabled"); self.chat.pack()
        self.entry=tk.Entry(root); self.entry.pack()

        tk.Button(root,text="Enviar",command=self.send_chat).pack()
        tk.Button(root,text="Desistir",fg="red",command=lambda:self.send("QUIT")).pack()

        self.sock=socket.socket(); self.sock.connect((HOST,PORT))
        threading.Thread(target=self.loop,daemon=True).start()

    def send(self,msg):
        self.sock.send((msg+"\n<END>\n").encode())

    def recv(self):
        d=""
        while "<END>" not in d:
            d+=self.sock.recv(1024).decode()
        return d.replace("\n<END>\n","")

    def loop(self):
        while True:
            self.root.after(0,self.update,self.recv())

    def update(self,data):
        self.last_data=data

        if data.startswith("[Chat]"):
            self.chat.config(state="normal")
            self.chat.insert(tk.END,data+"\n")
            self.chat.config(state="disabled")
            return

        if data.startswith("REMOVE"):
            self.awaiting_remove=True
            self.can_play=True
            self.status["text"]="Remover peça"
            return

        if "venceu" in data:
            self.status["text"]=data
            self.can_play=False
            return

        self.selected=None
        self.can_play=False

        lines=data.split("\n")

        for i in range(ROWS):
            for j,val in enumerate(lines[i].split()):
                self.buttons[i][j]["text"]=val
                self.buttons[i][j]["bg"]="lightcoral" if val=="X" else "lightblue" if val=="O" else "white"

        if "Jogador: O" in data:
            self.can_play=True

        self.status["text"]=data

    def click(self,r,c):
        if not self.can_play: return

        if self.awaiting_remove:
            self.send(f"{r} {c}")
            self.awaiting_remove=False
            self.can_play=False
            return

        if "placement" in self.last_data:
            self.send(f"MOVE {r} {c}")
            self.can_play=False
        else:
            if not self.selected:
                self.selected=(r,c)
            else:
                fr,fc=self.selected
                self.send(f"MOVE {fr} {fc} {r} {c}")
                self.selected=None
                self.can_play=False

    def send_chat(self):
        if self.entry.get():
            self.send("CHAT "+self.entry.get())
            self.entry.delete(0,tk.END)

root=tk.Tk()
DaraUI(root)
root.mainloop()