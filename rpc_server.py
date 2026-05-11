from xmlrpc.server import SimpleXMLRPCServer
from game import DaraGame

# =========================
# INICIAR JOGO
# =========================
game = DaraGame()

# =========================
# RPC METHODS
# =========================

def get_state():
    return game.get_state()


def place_piece(player, row, col):
    return game.place_piece(player, row, col)


def move_piece(player, fr, fc, tr, tc):
    return game.move_piece(player, fr, fc, tr, tc)


def remove_piece(player, row, col):
    return game.remove_piece(player, row, col)


def send_chat(player, message):
    return game.send_chat(player, message)


def quit_game(player):
    return game.quit_game(player)


# =========================
# SERVIDOR RPC
# =========================
server = SimpleXMLRPCServer(
    ("0.0.0.0", 8000),
    allow_none=True
)

print("Servidor RPC iniciado na porta 8000...")

# =========================
# REGISTRAR FUNÇÕES
# =========================
server.register_function(get_state, "get_state")

server.register_function(place_piece, "place_piece")

server.register_function(move_piece, "move_piece")

server.register_function(remove_piece, "remove_piece")

server.register_function(send_chat, "send_chat")

server.register_function(quit_game, "quit_game")

# =========================
# LOOP
# =========================
server.serve_forever()