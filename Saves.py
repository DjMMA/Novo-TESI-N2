from tkinter import *
from tkinter import ttk as ttk
from Criar_persona import Criar_persona

class Saves():
    def __init__(self, root):
        self.janela=root
        
        self.lbl_frm_1=LabelFrame(self.janela, text='Slot 1:')
        btn_sv1=Button(self.lbl_frm_1, text='Criar personagem', command=self.criar_persona)
        btn_sv1.grid(row=0,column=0, padx=5, pady=6)
        self.lbl_frm_1.grid(row=0,column=0, padx=5, pady=6)
        
    def criar_persona(self):
        self.limpar_tela()
        
        Criar_persona(self.janela)

    def limpar_tela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

