import tkinter as tk
from tkinter import ttk
import Dicio
from bdcria import conecta, SELECT_ALL_CLASSES, SELECT_ALL_RACAS
import sqlite3
from gerarnumale import Combate


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

        Raças = ['Humano', 'Elfo', 'Demônio', 'Orc']
        self.cbx_racas= ttk.Combobox(self.persona, values = Raças, state = 'readonly')
        self.cbx_racas.grid(row = 3, column= 1, columnspan=5)
        
        self.cbx_racas.bind('<<ComboboxSelected>>', self.get_attrs)

        lbl_classe = tk.Label (self.persona, text='Escolha sua classe!')
        lbl_classe.grid(row = 4, column= 1, columnspan=5)

        Classes = ['Guerreiro', 'Feiticeiro', 'Bardo', 'Ladino']
        self.cbx_classe = ttk.Combobox(self.persona, values = Classes, state = 'readonly')
        self.cbx_classe.grid(row = 5, column= 1, columnspan=5)

        self.cbx_classe.bind('<<ComboboxSelected>>', self.class_attr)

        self.persona.grid(row=0,column=1)
        #---------------------------------------------------------------------------------------------------------------
        
        #atributos------------------------------------------------------------------------------------------------------
        self.atributos=tk.LabelFrame(self.frm, text='Atributos')
        

        lbl_pontos = tk.Label (self.atributos, text='Distribua seus pontos!')
        lbl_pontos.grid(row = 0, column= 0, columnspan=5)

        self.var=tk.IntVar()

        self.con = tk.Spinbox(self.atributos, textvariable=self.var, from_=0, to=20, width=3)
        self.con.grid(row = 1, column= 0)

        lbl_con = tk.Label(self.atributos, text='Constituição')
        lbl_con.grid(row=1,column=1)

        self.var1=tk.IntVar()

        self.For = tk.Spinbox(self.atributos, textvariable=self.var1, from_=0, to=20, width=3)
        self.For.grid(row = 2, column= 0)

        lbl_For = tk.Label(self.atributos, text='Força')
        lbl_For.grid(row=2,column=1)

        self.var2=tk.IntVar()

        self.int = tk.Spinbox(self.atributos, textvariable=self.var2, from_=0, to=20, width=3)
        self.int.grid(row = 3, column= 0)

        lbl_int = tk.Label(self.atributos, text='Inteligência')
        lbl_int.grid(row=3,column=1)

        self.var3=tk.IntVar()

        self.car = tk.Spinbox(self.atributos, textvariable=self.var3, from_=0, to=20, width=3)
        self.car.grid(row = 4, column= 0)

        lbl_car = tk.Label(self.atributos, text='Carisma')
        lbl_car.grid(row=4,column=1)

        self.var4=tk.IntVar()

        self.agi = tk.Spinbox(self.atributos, textvariable=self.var4, from_=0, to=20, width=3)
        self.agi.grid(row = 5, column= 0)

        lbl_agi = tk.Label(self.atributos, text='Agilidade')
        lbl_agi.grid(row=5,column=1)

        self.atributos.grid(row=0,column=0)
        
        #---------------------------------------------------------------------------------------------------------------
        bnt_criar = tk.Button (self.frm, text='Criar', command=self.combate)
        bnt_criar.grid(row = 6, column= 0, columnspan=2, ipadx=15, pady=10)
        
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
        

        race=Dicio.RACES[self.race]
        print(race)
        id=0
        list_attr=[self.con, self.For, self.int, self.car, self.agi]
        list_var=[self.var, self.var1, self.var2, self.var3, self.var4]
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
        list_attr=[self.con, self.For, self.int, self.car, self.agi]
        list_var=[self.var, self.var1, self.var2, self.var3, self.var4]
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

