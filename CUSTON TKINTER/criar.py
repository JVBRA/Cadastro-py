from logging import PlaceHolder
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
#----------------------------------
import openpyxl as xl
#----------------------------------

janela_user=ctk.CTk()
janela_user.geometry("500X500")
list_user= 0
list_key= 0
def concluir():
    newemail = email_criar.get() 
    newsenha = senha_criar.get()
    email_criar.delete(0, ctk.END) 
    senha_criar.delete(0, ctk.END)
    #------------------------------------------------------------------------------
    import openpyxl as xl

    # Criar um novo livro
    book = xl.Workbook()

    # Adicionar uma planilha chamada 'usernames'
    user_page = book.create_sheet('usernames')

    # Adicionar cabeçalhos à planilha
    user_page.append(['E-mail','Senha'])

    # Coletar dados do usuário e adicioná-los à planilha
    user_page.append([newemail, newsenha])

    # Salvar o livro como "planilha_user.xlsx"
    #------------------------------------------------------------------------------ 
    if newemail and newsenha:
        list_user == newemail
        list_key == newsenha
        messagebox.showinfo("Mensagem", "Usuario cadastrado!")
        book.save("planilha_user.xlsx")
    else:
        messagebox.showinfo("Erro","Usuario não cadastrado!")
    janela_user.destroy()
  


texto = ctk.CTkLabel(janela_user, text="Criar Login")
texto.pack(padx=10, pady=10)

email_criar = ctk.CTkEntry(janela_user, placeholder_text="Seu Email")
email_criar.pack(padx=10, pady=10)
newemail = email_criar.get()


senha_criar= ctk.CTkEntry(janela_user, placeholder_text="Sua Senha",show="*")
senha_criar.pack(padx=10, pady=10)


botao_criar = ctk.CTkButton(janela_user, text="Concluir", command=concluir)
botao_criar.pack(padx=40, pady=40)


janela_user.mainloop()

