import socket

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

#  FUNÇÃO PADRÃO DE ENVIO
def send_msg(sock, msg):
    sock.send((msg + "\n<END>\n").encode())

#  FUNÇÃO PADRÃO DE RECEBIMENTO
def recv_msg(sock):
    data = ""
    while "<END>" not in data:
        data += sock.recv(1024).decode()
    return data.replace("\n<END>\n", "")

while True:
    data = recv_msg(client)
    print("\n" + data)

    # só joga se for realmente a vez dele
    if "Jogador: O" in data and "Fase" in data:
        print("\nComandos:")
        print("MOVE linha coluna")
        print("MOVE de_linha de_coluna para_linha para_coluna")
        print("CHAT mensagem")
        print("QUIT")

        msg = input("Sua vez: ")
        send_msg(client, msg)

    else:
        print("Aguardando o servidor...")