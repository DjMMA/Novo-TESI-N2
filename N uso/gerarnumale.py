import tkinter as tk
from tkinter import Button, Toplevel, Text, Scrollbar
import random

class Combate:
    def __init__(self, root):
        self.janela = root
        self.janela.title("Jogo de Combate")
        
        # Inicializa a vida do jogador e do monstro
        self.vida_jogador = 50
        self.vida_monstro = 50
        
        # Cria uma lista para armazenar o histórico
        self.historico = []

        # Criação da interface gráfica
        self.criar_interface()
        
    def criar_interface(self):
        # Labels para exibir a vida do jogador e do monstro
        self.vida_jogador_label = tk.Label(self.janela, text=f"Vida do Jogador: {self.vida_jogador}")
        self.vida_jogador_label.pack()
        self.vida_monstro_label = tk.Label(self.janela, text=f"Vida do Monstro: {self.vida_monstro}")
        self.vida_monstro_label.pack()

        # Rótulo para exibir o resultado
        self.resultado_label = tk.Label(self.janela, text="", font=("Helvetica", 16))
        self.resultado_label.pack()

        # Botão para iniciar o combate
        self.bnt_iniciar_combate = Button(self.janela, text='Iniciar Combate', command=self.iniciar_combate)
        self.bnt_iniciar_combate.pack()

        # Botão para exibir o histórico
        self.btn_historico = Button(self.janela, text='Histórico', command=self.exibir_historico)
        self.btn_historico.pack()

    def iniciar_combate(self):
        jogador = random.randint(1, 20)
        monstro = random.randint(1, 20)

        resultado = None
        
        if jogador > monstro:
            resultado = 'Você acertou seu ataque!'
            self.historico.append(resultado)
            self.gerar_dano_ataque()
        else:
            if monstro <= 10:
                resultado = 'Sua armadura lhe ajudou, o dano do monstro foi bloqueado!'
                self.historico.append("Dano de ataque bloqueado pelo jogador.")
            else:
                resultado = 'O monstro lhe atacou!'
                self.historico.append(resultado)
                self.gerar_dano_sofrido()

        
        # Verifique se a vida do jogador ou do monstro chegou a zero
        if self.vida_jogador <= 0:
            resultado = 'Você perdeu! O monstro ganhou!'
            self.historico.append(resultado)
            self.resultado_label.config(text=resultado)
            self.bnt_iniciar_combate.config(state=tk.DISABLED)  # Desabilita o botão de iniciar combate
        elif self.vida_monstro <= 0:
            resultado = 'Você ganhou! O monstro foi derrotado!'
            self.historico.append(resultado)
            self.resultado_label.config(text=resultado)
            self.bnt_iniciar_combate.config(state=tk.DISABLED)  # Desabilita o botão de iniciar combate

            
        # Cria uma nova janela para exibir o resultado da batalha
        resultado_janela = Toplevel(self.janela)
        resultado_janela.title("Resultado da Batalha")

        resultado_label = tk.Label(resultado_janela, text=resultado)
        resultado_label.pack()

        

    def gerar_dano_ataque(self):
        dano_ataque = random.randint(1, 20)

        if dano_ataque <= 5:
            resultado_janela = Toplevel(self.janela)
            resultado_janela.title("Dano de Ataque Fraco")
            resultado_label2 = tk.Label(resultado_janela, text="Seu dano foi muito fraco, o monstro nem sentiu!")
            resultado_label2.pack()

            self.historico.append(f"Dano de ataque = {dano_ataque}, bloqueado pelo monstro.")
        else:
            resultado_janela = Toplevel(self.janela)
            resultado_janela.title("Acerto no Ataque")
            resultado_label2 = tk.Label(resultado_janela, text=f"Dano de Ataque: {dano_ataque}")
            resultado_label2.pack()
            
            self.historico.append(f"Dano Ataque: {dano_ataque}")

        self.vida_monstro -= dano_ataque
        self.atualizar_vida()

    def gerar_dano_sofrido(self):
        dano_sofrido = random.randint(1, 20)
        resultado_janela = Toplevel(self.janela)
        resultado_janela.title("Erro no Ataque")
        resultado_label3 = tk.Label(resultado_janela, text=f"Dano Sofrido: {dano_sofrido}")
        resultado_label3.pack()

        self.historico.append(f"Dano Sofrido: {dano_sofrido}")

        self.vida_jogador -= dano_sofrido
        self.atualizar_vida()

    def atualizar_vida(self):
        self.vida_jogador_label.config(text=f"Vida do Jogador: {self.vida_jogador}")
        self.vida_monstro_label.config(text=f"Vida do Monstro: {self.vida_monstro}")

    def save_selecao(self):
        print('Seleção Salva')

    def exibir_historico(self):
        historico_janela = Toplevel(self.janela)
        historico_janela.title("Histórico da Partida")

        historico_text = Text(historico_janela, wrap=tk.WORD)
        historico_text.pack(fill=tk.BOTH, expand=True)

        scrollbar = Scrollbar(historico_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        for registro in self.historico:
            historico_text.insert(tk.END, registro + '\n')

        historico_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=historico_text.yview)

if __name__ == "__main__":
    janela = tk.Tk()
    combate = Combate(janela)
    janela.mainloop()
