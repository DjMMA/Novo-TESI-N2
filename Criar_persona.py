import tkinter as tk
from tkinter import ttk
import Dicio
import sqlite3
from gerarnumale import Combate
from banco_de_dados.classes import insere_valores



class Criar_persona():
        
    def Criou(self):
        self.lbl_frm_1.configure(text=self.name.get(), command=self.save_slct)
        self.btn_sv1.configure(text=self.name.get())
        self.janela.destroy()

    def __init__(self, root):

        self.janela=root
        print(type(self.janela))
        self.frm=tk.LabelFrame(self.janela, text='Personagem:')

        #caracteristicas-------------------------------------------------------------------------------------------------
        
        self.persona=tk.LabelFrame(self.frm, text='Características:')
        
        lbl_ent_name= tk.Label (self.persona, text= 'Nome:')
        lbl_ent_name.grid(row=0, column=1, columnspan=5)

        self.name = tk.Entry (self.persona)
        self.name.grid(row = 1, column= 1, columnspan=5)

        lbl_raca = tk.Label (self.persona, text='Escolha sua raça!')
        lbl_raca.grid(row = 2, column= 1, columnspan=5)

        Raças = ['Humano']
        self.cbx_racas= ttk.Combobox(self.persona, values = Raças, state = 'readonly')
        self.cbx_racas.grid(row = 3, column= 1, columnspan=5)
        
        self.cbx_racas.bind('<<ComboboxSelected>>', self.get_attrs)

        lbl_classe = tk.Label (self.persona, text='Escolha sua classe!')
        lbl_classe.grid(row = 4, column= 1, columnspan=5)

        Classes = ['Guerreiro', 'Mago', 'Nenhum']
        self.cbx_classe = ttk.Combobox(self.persona, values = Classes, state = 'readonly')
        self.cbx_classe.grid(row = 5, column= 1, columnspan=5)

        self.cbx_classe.bind('<<ComboboxSelected>>', self.class_attr)

        self.persona.grid(row=0,column=1)
        #---------------------------------------------------------------------------------------------------------------
        
        #atributos------------------------------------------------------------------------------------------------------
        self.atributos=tk.LabelFrame(self.frm, text='Atributos')
        

        lbl_pontos = tk.Label (self.atributos, text='Estes são seus pontos!')
        lbl_pontos.grid(row = 0, column= 0, columnspan=5)

        self.var=tk.IntVar()

        self.vida = tk.Spinbox(self.atributos, textvariable=self.var, from_=0, to=80, width=3)
        self.vida.grid(row = 1, column= 0)

        lbl_vida = tk.Label(self.atributos, text='Vida')
        lbl_vida.grid(row=1,column=1)

        self.var1=tk.IntVar()

        self.ataq = tk.Spinbox(self.atributos, textvariable=self.var1, from_=0, to=80, width=3)
        self.ataq.grid(row = 2, column= 0)

        lbl_ataq = tk.Label(self.atributos, text='Ataque')
        lbl_ataq.grid(row=2,column=1)

        self.var2=tk.IntVar()

        self.defe = tk.Spinbox(self.atributos, textvariable=self.var2, from_=0, to=80, width=3)
        self.defe.grid(row = 3, column= 0)

        lbl_defe = tk.Label(self.atributos, text='Defesa')
        lbl_defe.grid(row=3,column=1)

        self.var3=tk.IntVar()
        
        self.atributos.grid(row=0, column=0)
        #---------------------------------------------------------------------------------------------------------------
        bnt_criar = tk.Button (self.frm, text='Criar', command=self.valores)
        bnt_criar.grid(row = 5, column= 0, columnspan=2, ipadx=15, pady=10)
        
        self.frm.grid(row=0, column=0)

    def valores(self):
        self.limpar_tela()
        insere_valores()
        
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
        

        race=Dicio.RACES[self.race]
        print(race)
        id=0
        list_attr=[self.vida, self.ataq, self.defe]
        list_var=[self.var, self.var1, self.var2, self.var3]
        for value in race.values():
            list_attr[id].config(from_=value)
            list_var[id].set(value)
            id+=1
        self.cbx_classe.config(state='readonly')


    def class_attr(self, event = None):
        self.classe=self.cbx_classe.get()
    
        attr=Dicio.CLASSES[self.classe]
        print(attr)

        id=0
        v=[]
        list_attr=[self.vida, self.ataq, self.defe]
        list_var=[self.var, self.var1, self.var2, self.var3]
        for i in list_attr:
            x=int(list_attr[id].get())
            v.append(x)
        
        id=0
        for value in attr.values():
            x=int(v[id])
            x+=int(value)
            list_attr[id].config(from_=x)
            list_var[id].set(x)
            id+=1

    def get_classe_selecionada(self):
        return self.cbx_classe.get()
