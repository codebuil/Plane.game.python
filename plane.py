import tkinter as tk
import time
import random

# Configurações da janela
janela = tk.Tk()
janela.title("Jogo do Avião")
janela.geometry("800x400")
janela.configure(bg="lightyellow")
janela.resizable(False, False)

# Configuração da grade 16x16
for i in range(16):
    janela.grid_columnconfigure(i, weight=1)

# Inicialização das coordenadas do avião
aviao_x, aviao_y = 0, 7

# Inicialização das bolas
bolas = []

# Inicialização do score
score = 0

# Função para criar uma nova bola
def criar_bola():
    nova_bola = {
        'x': 15,
        'y': random.randint(0, 15)
    }
    bolas.append(nova_bola)

# Função para mover as bolas
def mover_bolas():
    for bola in bolas:
        bola['x'] -= 1

# Função para verificar colisões
def verificar_colisoes():
    global score

    for bola in bolas:
        if bola['x'] == aviao_x and bola['y'] == aviao_y:
            score -= 5
            bolas.remove(bola)

# Função para desenhar o jogo
def desenhar_jogo():
    # Limpar a tela
    tela.delete("all")

    # Desenhar o avião
    tela.create_text(aviao_x * 50 + 25, aviao_y * 25 + 12.5, text="✈", font=("Terminal", 20), fill="yellow")

    # Desenhar as bolas
    for bola in bolas:
        tela.create_text(bola['x'] * 50 + 25, bola['y'] * 25 + 12.5, text="●", font=("Terminal", 20), fill="yellow")

    # Atualizar o score na barra de título
    janela.title(f"Jogo do Avião - Score: {score}")

    # Verificar colisões
    verificar_colisoes()

    # Mover as bolas
    mover_bolas()

    # Criar uma nova bola aleatoriamente
    if random.random() < 0.1:
        criar_bola()

    # Chamar a função novamente após um intervalo de tempo
    janela.after(100, desenhar_jogo)

# Criar uma tela para desenhar o jogo
tela = tk.Canvas(janela, width=800, height=400, bg="lightyellow")
tela.pack()

# Registrar a função para eventos de teclado (movimento vertical do avião)
def mover_aviao(event):
    global aviao_y

    if event.keysym == "Up" and aviao_y > 0:
        aviao_y -= 1
    elif event.keysym == "Down" and aviao_y < 15:
        aviao_y += 1

janela.bind("<Up>", mover_aviao)
janela.bind("<Down>", mover_aviao)

# Inicializar o jogo
desenhar_jogo()

janela.mainloop()
