from tkinter import*
from ttkbootstrap import Style
from tkinter import messagebox as messagebox
from Saves import Saves

class save_slct():

    # Função que irá carregar o save do SQL, mostrando o mapa na tela e fechando as outras janelas
    def load_save(self):
        pass
    
    # Funçãp que irá remover o save do SQL, apagando todos os seus dados permanentemente
    def del_save(self):
        pass
    
    # Função simples que retornará para a tela de escolha de saves
    def voltar(self):
        pass

    def __init__(self, root):
        self.janela_save_sclt = root
        
        btn_carregar = Button(text="Carregar jogo", command=self.load_save).grid(row=0,column=0, padx=5, pady=6)
        btn_deletar = Button(text="Deletar ficha", command=self.del_save).grid(row=0,column=2, padx=5, pady=6)
        btn_voltar = Button(text="Voltar ao menu", command=self.voltar).grid(row=0,column=4, padx=5, pady=6)


