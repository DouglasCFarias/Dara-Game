
---

## 📌 Descrição

O projeto consiste em uma implementação completa do jogo **Dara**, permitindo que dois jogadores joguem em tempo real através de uma conexão de rede.

A aplicação foi desenvolvida em Python e segue o modelo **cliente-servidor**, onde:

- O **servidor** controla toda a lógica do jogo
- O **cliente** é responsável pela interface e interação com o usuário

---

## 🧠 Tecnologias Utilizadas

- Python 3
- Sockets (TCP/IP)
- Tkinter (Interface gráfica)
- Programação orientada a objetos

---

## 🏗️ Arquitetura do Sistema

O sistema foi dividido em camadas para garantir organização e desacoplamento:

UI (Tkinter)
↓
Cliente (Socket)
↓
Servidor
↓
Lógica do Jogo (game.py)

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

### 1️⃣ Iniciar o servidor

```bash
python server.py
python ui_client.py 
