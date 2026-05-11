
---

## 📌 Descrição

O sistema implementa o jogo Dara com:

- Comunicação distribuída via RPC
- Controle centralizado do estado do jogo
- Chat em tempo real
- Controle automático de turnos

O servidor é responsável por manter toda a lógica e sincronização do jogo, enquanto os clientes apenas realizam chamadas remotas para interação.

---

## 🧠 Tecnologias Utilizadas

- Python 3
- XML-RPC
- Tkinter
- Programação Orientada a Objetos

---

## 🏗️ Arquitetura do Sistema

O sistema utiliza arquitetura cliente-servidor baseada em RPC.

---

## 🎮 Funcionalidades

✔️ Jogo Dara completo  
✔️ Controle de turno automático  
✔️ Duas fases do jogo:
- Fase de colocação
- Fase de movimentação  

✔️ Regra de formação de 3 peças  
✔️ Remoção de peças do adversário  
✔️ Detecção de vitória  
✔️ Chat em tempo real entre jogadores  
✔️ Desistência da partida  
✔️ Interface gráfica interativa  

---

## 🚀 Como Executar

1️⃣ Iniciar o servidor RPC

python rpc_server.py

Você verá:

Servidor RPC iniciado na porta 8000...

2️⃣ Abrir a interface do jogador X

python rpc_client_x.py

3️⃣ Abrir a interface do jogador O

python rpc_client_o.py

---
🎯 Como Jogar

🧩 Fase de Colocação

Os jogadores posicionam suas peças alternadamente no tabuleiro.

🔄 Fase de Movimentação

Após posicionarem todas as peças:

1. selecione uma peça
2. mova para uma posição adjacente

❌ Captura

Ao formar 3 peças em linha:

o jogador pode remover uma peça adversária

💬 Chat

Os jogadores podem trocar mensagens em tempo real durante a partida.

🚪 Desistência

O jogador pode desistir a qualquer momento utilizando o botão "Desistir".

---

🔌 RPC (Remote Procedure Call)

A comunicação do sistema foi implementada utilizando XML-RPC.

O servidor expõe funções remotas como:

place_piece()

move_piece()

remove_piece()

send_chat()

get_state()

quit_game()

Os clientes utilizam ServerProxy para invocar esses métodos remotamente.




