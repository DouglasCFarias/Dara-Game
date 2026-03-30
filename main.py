from game import DaraGame

game = DaraGame()

while True:
    game.print_board()
    print(f"Jogador {game.current_player}")
    print(f"Fase: {game.phase}")

    if game.phase == "placement":
        row = int(input("Linha: "))
        col = int(input("Coluna: "))
        game.place_piece(row, col)

    else:
        print("Mover peça:")
        fr = int(input("De linha: "))
        fc = int(input("De coluna: "))
        tr = int(input("Para linha: "))
        tc = int(input("Para coluna: "))
        game.move_piece(fr, fc, tr, tc)

    winner = game.check_winner()
    if winner:
        print(f"Jogador {winner} venceu!")
        break