import customtkinter as ctk
from tkinter import ttk
import datetime as dt
from tkinter import messagebox

janela_cadastro= ctk.CTk()

lista_tipos = ["Galão","Caixa","Saco"]
unidades= ["Kg","Unidade"]
lista_codigos=[]
#------------------------------------------------------------------------------------------------------------------
def inserir_codigo():
    messagebox.showinfo("Mensagem", "Codigo foi adicionado!")
    descricao = entry_descricao.get()
    tipo = combobox_selecionar_tipo.get()
    quant = entry_quant.get()
    peso = entry_peso.get()
    lote = entry_lote.get()
    unid = entry_unidademedida.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime("%d/%m/%Y %H:%M")
    codigo = len(lista_codigos)+1
    codigo_str = "COD-{}".format(codigo)
    lista_codigos.append((codigo_str,descricao,tipo,quant,data_criacao,peso))
    messagebox.showinfo("Aviso!","Codigo cadastrado com Sucesso!")

#------------------------------------------------------------------------------------------------------------------
janela_cadastro.title('Ferramenta de cadastro de materiais')

label_descricao = ctk.CTkLabel(janela_cadastro, text="Criar Login")
label_descricao.grid(row=1, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )

entry_descricao = ctk.CTkEntry(janela_cadastro)
entry_descricao.grid(row=2,column=0, padx=10, pady=10, sticky='nswe', columnspan = 4)

label_tipo_unidade = ctk.CTkLabel(janela_cadastro, text="Tipo da unidade do Material")
label_tipo_unidade.grid(row=3, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )

combobox_selecionar_tipo = ctk.CTkComboBox(janela_cadastro, values=lista_tipos)
combobox_selecionar_tipo.grid(row=3, column=2, padx = 10, pady=10, sticky='nswe', columnspan = 2)

label_quant =  ctk.CTkLabel(janela_cadastro, text="Quantidade na unidade de matetial")
label_quant.grid(row=4, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_quant =  ctk.CTkComboBox(janela_cadastro, values=unidades)
entry_quant.grid(row=4, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

label_peso =  ctk.CTkLabel(janela_cadastro, text="Peso")
label_peso.grid(row=5, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_peso =  ctk.CTkEntry(janela_cadastro)
entry_peso.grid(row=5, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

label_unidade =  ctk.CTkLabel(janela_cadastro, text="Unidade de medida")
label_unidade.grid(row=6, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_unidademedida =  ctk.CTkEntry(janela_cadastro)
entry_unidademedida.grid(row=6, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

label_lote =  ctk.CTkLabel(janela_cadastro, text="Lote")
label_lote.grid(row=7, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )
entry_lote =  ctk.CTkEntry(janela_cadastro)
entry_lote.grid(row=7, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

botao_criar_codigo = ctk.CTkButton(janela_cadastro, text="Criar código", command=inserir_codigo)
botao_criar_codigo.grid(row=8,column=0,padx = 10, pady=10,sticky='nswe', columnspan =4)




janela_cadastro.mainloop()