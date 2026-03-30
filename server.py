import socket
from game import DaraGame

HOST = '0.0.0.0'
PORT = 5000

game = DaraGame()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Aguardando conexão...")
conn, addr = server.accept()
print(f"Conectado com {addr}")

def send_msg(msg):
    conn.send((msg + "\n<END>\n").encode())

def recv_msg():
    data = ""
    while "<END>" not in data:
        data += conn.recv(1024).decode()
    return data.replace("\n<END>\n", "")

def board():
    return "\n".join([" ".join(r) for r in game.board])

def send_state():
    send_msg(f"{board()}\nJogador: {game.current_player}\nFase: {game.phase}")

while True:
    send_state()

    if game.current_player == "X":
        msg = input("Sua vez (X): ")
    else:
        msg = recv_msg()

    try:
        if msg.startswith("QUIT"):
            winner = "O" if game.current_player == "X" else "X"
            send_msg(f"Jogador {winner} venceu por desistência!")
            break

        if msg.startswith("CHAT"):
            send_msg(f"[Chat] {msg[5:]}")
            continue

        if msg.startswith("MOVE"):
            parts = msg.split()[1:]

            if game.phase == "placement":
                if not game.place_piece(*map(int, parts)):
                    send_msg("Jogada inválida")
                    continue

            else:
                result = game.move_piece(*map(int, parts))

                if result == "REMOVE":
                    send_msg("REMOVE")
                    r, c = map(int, recv_msg().split())

                    if game.remove_opponent_piece(r, c):
                        game.finalize_turn()
                    else:
                        send_msg("Remoção inválida")
                        continue

                elif result:
                    game.finalize_turn()
                else:
                    send_msg("Movimento inválido")
                    continue

        winner = game.check_winner()
        if winner:
            send_msg(f"Jogador {winner} venceu!")
            break

    except:
        send_msg("Erro na jogada")

conn.close()
server.close()