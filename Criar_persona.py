import tkinter as tk
from tkinter import ttk
import sqlite3
import banco_de_dados.racas as bd_racas 
import banco_de_dados.classes as bd_classes
from gerarnumale import Combate

class Criar_persona():
        
    def Criou(self):
        self.lbl_frm_1.configure(text=self.name.get(), command=self.save_slct)
        self.btn_sv1.configure(text=self.name.get())
        self.janela.destroy()

    def __init__(self, root):

        self.janela=root
        self.frm=tk.LabelFrame(self.janela, text='Personagem:')

        #caracteristicas-------------------------------------------------------------------------------------------------
        
        self.persona=tk.LabelFrame(self.frm, text='Características:')
        
        lbl_ent_name= tk.Label (self.persona, text= 'Nome:')
        lbl_ent_name.grid(row=0, column=1, columnspan=5)

        self.name = tk.Entry (self.persona)
        self.name.grid(row = 1, column= 1, columnspan=5)

        lbl_raca = tk.Label (self.persona, text='Escolha sua raça!')
        lbl_raca.grid(row = 2, column= 1, columnspan=5)
        
        Raças = bd_racas.retorna_nome()
        self.cbx_racas= ttk.Combobox(self.persona, values = Raças, state = 'readonly')
        self.cbx_racas.grid(row = 3, column= 1, columnspan=5)
        
        self.cbx_racas.bind('<<ComboboxSelected>>', self.get_attrs)

        lbl_classe = tk.Label (self.persona, text='Escolha sua classe!')
        lbl_classe.grid(row = 4, column= 1, columnspan=5)

        Classes = bd_classes.retorna_nomes()
        self.cbx_classe = ttk.Combobox(self.persona, values = Classes, state = 'readonly')
        self.cbx_classe.grid(row = 5, column= 1, columnspan=5)

        self.cbx_classe.bind('<<ComboboxSelected>>', self.class_attr)

        self.persona.grid(row=0,column=1)
        #---------------------------------------------------------------------------------------------------------------
        
        #atributos------------------------------------------------------------------------------------------------------
        self.atributos=tk.LabelFrame(self.frm, text='Atributos')
        
        lbl_pontos = tk.Label (self.atributos, text='Estes são seus pontos!')
        lbl_pontos.grid(row = 0, column= 0, columnspan=5)


        self.var1=tk.IntVar()
        # Classes = bd_classes.retorna_atributos()
        self.lbl_vida = tk.Label(self.atributos, text=0, width=3)
        self.lbl_vida.grid(row = 1, column= 0)
        lbl_nomevida = tk.Label(self.atributos, text='Vida')
        lbl_nomevida.grid(row=1,column=1)


        self.var2=tk.IntVar()
        self.lbl_ataq = tk.Label(self.atributos, text=0, width=3)
        self.lbl_ataq.grid(row = 2, column= 0)
        lbl_nomeataq = tk.Label(self.atributos, text='Ataque')
        lbl_nomeataq.grid(row=2,column=1)
        
        
        self.var3=tk.IntVar()
        self.lbl_defe = tk.Label(self.atributos, text=0, width=3)
        self.lbl_defe.grid(row = 3, column= 0)
        lbl_nomedefe = tk.Label(self.atributos, text='Defesa')
        lbl_nomedefe.grid(row=3,column=1)
        
        self.atributos.grid(row=0, column=0)
        #---------------------------------------------------------------------------------------------------------------
        bnt_criar = tk.Button (self.frm, text='Criar', command=self.combate)
        bnt_criar.grid(row = 5, column= 0, columnspan=2, ipadx=15, pady=10)
        
        self.frm.grid(row=0, column=0)
        
    def combate(self):
        self.limpar_tela()
        Combate(self.frm)
        
    def limpar_tela(self):
        for widget in self.frm.winfo_children():
            widget.destroy()
        
    def get_attrs(self, event = None):
        self.Name=self.name.get()
        self.race=self.cbx_racas.get()
        self.classe=self.cbx_classe.get()
    

    def class_attr(self, event = None):
        self.classe=self.cbx_classe.get()
        # classe = bd_classes.retorna_atributos(self.classe)
        # print(classe)
        vida_classe, ataque_classe, defesa_classe = bd_classes.retorna_atributos(self.classe)
        self.lbl_vida.config(text= vida_classe)
        self.lbl_ataq.config(text= ataque_classe)
        self.lbl_defe.config(text= defesa_classe)


    def get_classe_selecionada(self):
        return self.cbx_classe.get()
