import tkinter as tk
from tkinter import Button, Label, Toplevel, Text, Scrollbar
import random

class Combate():
    def __init__(self, root):
        self.janela = root
        self.frm = tk.LabelFrame(self.janela, text='Personagem:')
        self.name = tk.StringVar()
        self.lbl_frm_1 = tk.Label(self.frm, textvariable=self.name)
        self.lbl_frm_1.pack()
        
        self.btn_sv1 = Button(self.frm, text='Salvar Seleção', command=self.save_slct)
        self.btn_sv1.pack()
        
        self.vida_jogador = 50  # Vida inicial do jogador
        self.vida_monstro = 50  # Vida inicial do monstro

        # Labels para exibir a vida do jogador e do monstro
        self.vida_jogador_label = Label(self.janela, text=f"Vida do Jogador: {self.vida_jogador}")
        self.vida_jogador_label.pack()
        self.vida_monstro_label = Label(self.janela, text=f"Vida do Monstro: {self.vida_monstro}")
        self.vida_monstro_label.pack()

        bnt_alterar = Button(self.janela, text='Iniciar combate', command=self.Batalha)
        bnt_alterar.pack()

        # Botão para exibir o histórico
        self.btn_historico = Button(self.janela, text='Histórico', command=self.exibir_historico)
        self.btn_historico.pack()

        # Inicializa o histórico como uma lista vazia
        self.historico = []
        

    def Batalha(self):
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

        # Registra o resultado no histórico
        self.historico.append(resultado)

        # Cria uma nova janela para exibir o resultado
        resultado_janela = Toplevel(self.janela)
        resultado_janela.title("Resultado da Batalha")

        resultado_label = Label(resultado_janela, text=resultado)
        resultado_label.pack()

    def gerar_dano_ataque(self):
        dano_ataque = random.randint(1, 20)

        if dano_ataque < 5:
            resultado_janela = Toplevel(self.janela)
            resultado_janela.title("Dano de Ataque Fraco")
            resultado_label2 = Label(resultado_janela, text="Seu dano foi muito fraco, o monstro nem sentiu!")
            resultado_label2.pack()
            self.historico.append("Dano de ataque bloqueado pelo monstro.")
        else:
            resultado_janela = Toplevel(self.janela)
            resultado_janela.title("Acerto no Ataque")
            resultado_label2 = Label(resultado_janela, text=f"Dano de Ataque: {dano_ataque}")
            resultado_label2.pack()

        # Reduz a vida do monstro com base no dano de ataque
        self.vida_monstro -= dano_ataque
        self.atualizar_vida()

    def gerar_dano_sofrido(self):
        dano_sofrido = random.randint(1, 20)
        resultado_janela = Toplevel(self.janela)
        resultado_janela.title("Ataque sofrido")
        resultado_label3 = Label(resultado_janela, text=f"Dano Sofrido: {dano_sofrido}")
        resultado_label3.pack()

        # Registra o dano sofrido no histórico
        self.historico.append(f"Dano Sofrido: {dano_sofrido}")

        # Reduz a vida do jogador com base no dano sofrido
        self.vida_jogador -= dano_sofrido
        self.atualizar_vida()

    def atualizar_vida(self):
        # Atualiza as variáveis da interface gráfica com as novas vidas
        self.vida_jogador_label.config(text=f"Vida do Jogador: {self.vida_jogador}")
        self.vida_monstro_label.config(text=f"Vida do Monstro: {self.vida_monstro}")

    def save_slct(self):
        print('Seleção Salva')

    def exibir_historico(self):
        # Cria uma janela para exibir o histórico
        historico_janela = Toplevel(self.janela)
        historico_janela.title("Histórico da Partida")

        # Cria um widget Text para exibir o histórico com uma barra de rolagem
        historico_text = Text(historico_janela, wrap=tk.WORD)
        historico_text.pack(fill=tk.BOTH, expand=True)

        scrollbar = Scrollbar(historico_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Adiciona o histórico ao widget Text
        for registro in self.historico:
            historico_text.insert(tk.END, registro + '\n')

        # Conecta a barra de rolagem ao widget Text
        historico_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=historico_text.yview)

if __name__ == "__main__":
    janela = tk.Tk()
    combate = Combate(janela)
    janela.mainloop()
