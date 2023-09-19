from tkinter import*
from ttkbootstrap import Style
from tkinter import messagebox as messagebox
from Saves import Saves
from banco_de_dados.users import insere_valores


class Cadastro_user():
    Users=[]
    def __init__(self, root):
        self.janela=root
        lbl = Label(self.janela, text="Bem-vindo(a), crie seu perfil aqui")
        lbl.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        self.ent_user = Entry(self.janela)
        self.ent_user.grid(row=1, column=1, padx=10, pady=5)
        lbl_user = Label(self.janela, text='Usuário:')
        lbl_user.grid(row=1, column=0, padx=10, pady=5)
        
        self.ent_senha = Entry(self.janela, show='*')
        self.ent_senha.grid(row=2, column=1, padx=10, pady=5)
        lbl_senha = Label(self.janela, text='Senha:')
        lbl_senha.grid(row=2, column=0, padx=10, pady=5)

        self.conf_senha = Entry(self.janela, show='*')
        self.conf_senha.grid(row=3, column=1, padx=10, pady=5)
        lbl_senha = Label(self.janela, text='Confirmar:')
        lbl_senha.grid(row=3, column=0, padx=10, pady=5)
        
        btn_logar = Button(self.janela, text='Entrar', command=self.cadastrar, width=15)
        btn_logar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def cadastrar(self):
        
        user=self.ent_user.get()
        senha=self.ent_senha.get()
        conf_senha=self.conf_senha.get()
        
        if user == '' or senha == '' or conf_senha == '':
            messagebox.showinfo('Aviso', 'Por favor, todos os campos são obrigatórios.', parent=self.janela)
        elif senha!=conf_senha:
            messagebox.showwarning('Aviso', 'As senhas não são correspondentes!!', parent=self.janela)
        else:
            insere_valores(user,senha)
            
            self.limpar_tela()
            Saves(self.janela, user)

        
    
    def limpar_tela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

        
        


        
       


