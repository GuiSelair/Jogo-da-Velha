# encoding: utf-8


# ------------------ JOGO DO VELHA ---------------------- #

velha = {"top-e": "1", "top-m": "2", "top-d": "3",
         "mid-e": "4", "mid-m": "5", "mid-d": "6",
         "bot-e": "7", "bot-m": "8", "bot-d": "9"}

turno = "X"

def mostraVelha():
    global velha
    print("\n")
    print(f"{velha['top-e']:^5}|{velha['top-m']:^5}|{velha['top-d']:^5}")
    print("-" * 5 + "+" + "-" * 5 + "+" + "-" * 5)
    print(f"{velha['mid-e']:^5}|{velha['mid-m']:^5}|{velha['mid-d']:^5}")
    print("-" * 5 + "+" + "-" * 5 + "+" + "-" * 5)
    print(f"{velha['bot-e']:^5}|{velha['bot-m']:^5}|{velha['bot-d']:^5}")

def verificaVitoria(t):
    global velha
    return ((velha["top-e"] == t and velha["top-m"] == t and velha["top-d"] == t) or
    (velha["mid-e"] == t and velha["mid-m"] == t and velha["mid-d"] == t) or
    (velha["bot-e"] == t and velha["bot-m"] == t and velha["bot-d"] == t) or
    (velha["top-e"] == t and velha["mid-m"] == t and velha["bot-d"] == t) or
    (velha["top-d"] == t and velha["mid-m"] == t and velha["bot-e"] == t) or
    (velha["top-e"] == t and velha["mid-e"] == t and velha["bot-e"] == t) or
    (velha["top-m"] == t and velha["mid-m"] == t and velha["bot-m"] == t) or
    (velha["top-d"] == t and velha["mid-d"] == t and velha["bot-d"] == t))


def inserir(escolha, turno):
    global velha
    if escolha == 1:
        velha["top-e"] = turno
    elif escolha == 2:
        velha["top-m"] = turno
    elif escolha == 3:
        velha["top-d"] = turno
    elif escolha == 4:
        velha["mid-e"] = turno
    elif escolha == 5:
        velha["mid-m"] = turno
    elif escolha == 6:
        velha["mid-d"] = turno
    elif escolha == 7:
        velha["bot-e"] = turno
    elif escolha == 8:
        velha["bot-m"] = turno
    elif escolha == 9:
        velha["bot-d"] = turno
    else:
        print("=== ERROR: Número errado. Perdeu a vez ===")

# -------------- JOGO -----------------
winner = False

for x in range(9):
    mostraVelha()
    escolha = int(input("\nDigite o código de onde quer inserir: "))
    inserir(escolha, turno)
    if turno == "X":
        if verificaVitoria(turno):
            mostraVelha()
            print(f"\n=== PARABÉNS!! O jogador {turno} ganhou o jogo ===")
            winner = True
            break
        turno = "O"
    else:
        if verificaVitoria(turno):
            mostraVelha()
            print(f"\n=== PARABÉNS!! O jogador {turno} ganhou o jogo ===")
            winner = True
            break
        turno = "X"
if not winner:
    print(f"\n === INFELIZMENTE!! NINGUEM GANHOU === ")
