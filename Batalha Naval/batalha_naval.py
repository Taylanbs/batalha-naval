import random

def criar_tabuleiro(tamanho):
    return [['~' for _ in range(tamanho)] for _ in range(tamanho)]

def imprimir_tabuleiro(tabuleiro, revelar=False):
    print("  " + " ".join(str(i) for i in range(len(tabuleiro))))
    for i, linha in enumerate(tabuleiro):
        if revelar:
            print(f"{i} " + " ".join(linha))
        else:
            print(f"{i} " + " ".join('X' if cel == 'N' else cel for cel in linha))

def posicionar_navios(tabuleiro, quantidade):
    tamanho = len(tabuleiro)
    navios = 0
    while navios < quantidade:
        x, y = random.randint(0, tamanho - 1), random.randint(0, tamanho - 1)
        if tabuleiro[x][y] == '~':
            tabuleiro[x][y] = 'N'
            navios += 1

def escolher_dificuldade():
    while True:
        try:
            print("\nEscolha a dificuldade:")
            print("1 - Fácil (7x7, 5 navios)")
            print("2 - Médio (5x5, 3 navios)")
            print("3 - Difícil (3x3, 2 navios)")
            escolha = int(input("Digite o número da dificuldade: "))
            if escolha == 1:
                return 7, 5
            elif escolha == 2:
                return 5, 3
            elif escolha == 3:
                return 3, 2
            else:
                print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida, tente novamente.")

def jogada_computador(tabuleiro):
    while True:
        x, y = random.randint(0, len(tabuleiro) - 1), random.randint(0, len(tabuleiro) - 1)
        if tabuleiro[x][y] in ('~', 'N'):
            return x, y

def jogar():
    tamanho, navios = escolher_dificuldade()
    tabuleiro_jogador = criar_tabuleiro(tamanho)
    tabuleiro_computador = criar_tabuleiro(tamanho)
    posicionar_navios(tabuleiro_computador, navios)
    tentativas_jogador = 0
    acertos_jogador = 0
    tentativas_computador = 0
    acertos_computador = 0

    print("\nBem-vindo ao Batalha Naval!")
    while acertos_jogador < navios and acertos_computador < navios:
        print("\nSeu tabuleiro:")
        imprimir_tabuleiro(tabuleiro_jogador)
        print("\nAtaque o tabuleiro do computador:")
        imprimir_tabuleiro(tabuleiro_computador)
        
        try:
            x = int(input("Digite a linha: "))
            y = int(input("Digite a coluna: "))
            if tabuleiro_computador[x][y] == 'N':
                print("\nAcertou um navio!")
                tabuleiro_computador[x][y] = 'X'
                acertos_jogador += 1
            elif tabuleiro_computador[x][y] == 'X' or tabuleiro_computador[x][y] == 'O':
                print("\nVocê já atirou aqui!")
            else:
                print("\nErrou!")
                tabuleiro_computador[x][y] = 'O'
            tentativas_jogador += 1
        except (ValueError, IndexError):
            print("\nEntrada inválida. Tente novamente.")
            continue
        
        print("\nVez do computador...")
        x, y = jogada_computador(tabuleiro_jogador)
        if tabuleiro_jogador[x][y] == 'N':
            print(f"Computador acertou na posição ({x}, {y})!")
            tabuleiro_jogador[x][y] = 'X'
            acertos_computador += 1
        else:
            print(f"Computador errou na posição ({x}, {y})!")
            tabuleiro_jogador[x][y] = 'O'
        tentativas_computador += 1
    
    if acertos_jogador == navios:
        print(f"\nParabéns! Você venceu em {tentativas_jogador} tentativas.")
    else:
        print(f"\nO computador venceu em {tentativas_computador} tentativas.")
    
    print("\nTabuleiro final do Computador:")
    imprimir_tabuleiro(tabuleiro_computador, revelar=True)
    print("\nTabuleiro final do Jogador:")
    imprimir_tabuleiro(tabuleiro_jogador, revelar=True)

if __name__ == "__main__":
    jogar()
