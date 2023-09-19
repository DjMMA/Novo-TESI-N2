from tkinter import *
from ttkbootstrap import Style
from Cadastro_user import Cadastro_user as Cad_User
from Saves import Saves as save
from banco_de_dados.users import seleciona_por_nome

class TelaPrincipal:

    def __init__(self, master):
        self.janela = master
        self.janela.title("Death's Valley")
        
        self.style = Style('superhero')
        
        self.frm_principal = Frame(self.janela)
        self.frm_principal.grid(row=0, column=0, padx=20, pady=20)

        self.login()

    def login(self):

        self.limpar_tela()
        lbl = Label(self.frm_principal, text="Bem-vindo(a) ao Death's Valley")
        lbl.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        self.ent_user = Entry(self.frm_principal)
        self.ent_user.grid(row=1, column=1, padx=10, pady=5)
        lbl_user = Label(self.frm_principal, text='Usuário:')
        lbl_user.grid(row=1, column=0, padx=10, pady=5)
        
        self.ent_senha = Entry(self.frm_principal, show='*')
        self.ent_senha.grid(row=2, column=1, padx=10, pady=5)
        lbl_senha = Label(self.frm_principal, text='Senha:')
        lbl_senha.grid(row=2, column=0, padx=10, pady=5)
        
        self.btn_logar = Button(self.frm_principal, text='Entrar', command=self.logar, width=15)
        self.btn_logar.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.btn_cadastrar=Button(self.frm_principal, text='Cadastrar',command=self.cadastrar, width=15)
        self.btn_cadastrar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def cadastrar(self):
        self.limpar_tela()
        Cad_User(self.frm_principal)
        
    def logar(self):
        self.user=self.ent_user.get()
        self.senha=self.ent_senha.get()
        senha_return = seleciona_por_nome(self.user)
        
        print(senha_return)
        if self.senha=='' or self.user=='':
            self.btn_logar.config(self.btn_logar.grid(row=4, column=0,columnspan=2))
            self.btn_cadastrar.config(self.btn_cadastrar.grid(row=5, column=0,columnspan=2))
            lbl_aviso=Label(self.frm_principal, text='Por favor, preencha todos os campos!')
            lbl_aviso.grid(row=3,column=0, columnspan=2)
            
        elif senha_return != self.senha:
            self.btn_logar.config(self.btn_logar.grid(row=4, column=0,columnspan=2))
            self.btn_cadastrar.config(self.btn_cadastrar.grid(row=5, column=0,columnspan=2))
            lbl_aviso=Label(self.frm_principal, text='Senha incorreta!')
            lbl_aviso.grid(row=3,column=0, columnspan=2)
            
        else:   
            self.limpar_tela()
            save(self.frm_principal, self.user)

            btn_voltar_menu=Button(self.frm_principal, text='Voltar', command=self.login)
            btn_voltar_menu.grid(row=1,column=1, columnspan=2, rowspan=2, padx=5, pady=5)

    def limpar_tela(self):
        for widget in self.frm_principal.winfo_children():
            widget.destroy()

app = Tk()
janela = TelaPrincipal(app)
app.mainloop()
