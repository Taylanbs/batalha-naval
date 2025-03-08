import tkinter as tk
import random

# Tamanhos do tabuleiro
tamanho = 5
navios = 3

def criar_tabuleiro():
    return [['~' for _ in range(tamanho)] for _ in range(tamanho)]

def posicionar_navios(tabuleiro, quantidade):
    for _ in range(quantidade):
        while True:
            x, y = random.randint(0, tamanho - 1), random.randint(0, tamanho - 1)
            if tabuleiro[x][y] == '~':
                tabuleiro[x][y] = 'N'
                break

def clique(x, y):
    global acertos
    if tabuleiro_computador[x][y] == 'N':
        botoes[x][y].config(text='X', bg='red')
        tabuleiro_computador[x][y] = 'X'
        acertos += 1
        if acertos == navios:
            resultado.config(text="Você venceu!")
    else:
        botoes[x][y].config(text='O', bg='blue')

tabuleiro_computador = criar_tabuleiro()
posicionar_navios(tabuleiro_computador, navios)
acertos = 0

# Interface Gráfica
root = tk.Tk()
root.title("Batalha Naval")

frame = tk.Frame(root)
frame.pack()

botoes = []
for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        btn = tk.Button(frame, text='~', width=4, height=2, command=lambda x=i, y=j: clique(x, y))
        btn.grid(row=i, column=j)
        linha.append(btn)
    botoes.append(linha)

resultado = tk.Label(root, text="", font=("Arial", 14))
resultado.pack()

root.mainloop()
