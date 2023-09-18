from tkinter import *
from tkinter import ttk as ttk

class Persona():
    def __init__(self,root):
        self.janela=root
        #Frame 0
        frame0 = LabelFrame(self.janela, text="Você é um:")
        frame0.grid(row=0, column=0)

        lbl_suaraca = Label(frame0, text="ORC")
        lbl_suaraca.pack()

        #Frame 1
        frame1 = LabelFrame(self.janela, text="A classe escolhida foi:")
        frame1.grid(row=0, column=1)

        lbl_suaclasse = Label(frame1, text="GUERREIRO")
        lbl_suaclasse.pack()

        #Frame 2
        frame2 = LabelFrame(self.janela, text="Pontos de atributos:")
        frame2.grid(row=1, column=0, columnspan=2)

        lbl_vocepontos = Label (frame2, text='Seus pontos distribuidos estão abaixo:')
        lbl_vocepontos.grid(row=1, column=0, columnspan=5)

        lbl_novospontos = Label (frame2, text='Ao derrotar monstros você ganha mais pontos para redistribuir.')
        lbl_novospontos.grid(row=2, column=0, columnspan=5)

        spb_vida = Spinbox(frame2, from_=0, to=8, wrap=True, width=3)
        spb_vida.grid(row=3, column=0)

        spb_ataq = Spinbox(frame2, from_=0, to=8, wrap=True, width=3)
        spb_ataq.grid(row=3, column=1)

        spb_defe = Spinbox(frame2, from_=0, to=8, wrap=True, width=3)
        spb_defe.grid(row=3, column=2)

        bnt_alterar = Button (self.janela, text='Confirmar alterações', command=self.janela.destroy)
        bnt_alterar.grid(row = 8, column= 0, columnspan=5)
