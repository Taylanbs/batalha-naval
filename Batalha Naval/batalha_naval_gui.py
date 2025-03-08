import tkinter as tk
import random

class BatalhaNaval:
    def __init__(self, root):
        self.root = root
        self.root.title("Batalha Naval")
        
        self.tamanho = 5  # Tamanho do tabuleiro
        self.navios = 3   # Quantidade de navios
        self.tabuleiro_computador = [['~' for _ in range(self.tamanho)] for _ in range(self.tamanho)]
        self.botoes = []
        
        self.posicionar_navios()
        self.criar_interface()
    
    def posicionar_navios(self):
        """Posiciona os navios aleatoriamente no tabuleiro do computador."""
        contador = 0
        while contador < self.navios:
            x, y = random.randint(0, self.tamanho - 1), random.randint(0, self.tamanho - 1)
            if self.tabuleiro_computador[x][y] == '~':
                self.tabuleiro_computador[x][y] = 'N'
                contador += 1
    
    def criar_interface(self):
        """Cria o tabuleiro visual."""
        frame = tk.Frame(self.root)
        frame.pack()
        
        for i in range(self.tamanho):
            linha_botoes = []
            for j in range(self.tamanho):
                botao = tk.Button(frame, text="~", width=4, height=2,
                                  command=lambda x=i, y=j: self.atacar(x, y))
                botao.grid(row=i, column=j)
                linha_botoes.append(botao)
            self.botoes.append(linha_botoes)
        
        self.mensagem = tk.Label(self.root, text="Escolha uma posição para atacar!")
        self.mensagem.pack()
    
    def atacar(self, x, y):
        """Realiza um ataque na posição escolhida pelo jogador."""
        if self.tabuleiro_computador[x][y] == 'N':
            self.botoes[x][y].config(text="X", bg="red")
            self.mensagem.config(text="Acertou um navio!")
        else:
            self.botoes[x][y].config(text="O", bg="blue")
            self.mensagem.config(text="Errou!")
        self.botoes[x][y].config(state=tk.DISABLED)  # Desativa o botão após o ataque

# Inicializa o jogo
root = tk.Tk()
jogo = BatalhaNaval(root)
root.mainloop()
