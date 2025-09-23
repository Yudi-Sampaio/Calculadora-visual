#calculadora visual computador

import tkinter as tk
from tkinter import ttk

#interface visual da calculadora
janela = tk.Tk()
janela.title("Calculadora Visual")
janela.geometry("320x420")
janela.resizable(False, False)

#campo de texto
entrada_var = tk.StringVar()
entrada = tk.Entry(janela, textvariable=entrada_var, width=20, font=('bold', 50), justify="left",bg = "#34495e" , fg = "white" , insertbackground = "white")
entrada.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
entrada.focus_set()

#botões de interação
def clicar(valor):
    entrada_var.set(entrada.get() + str(valor))

def limpar():
    entrada_var.set("")

def backspace():
    entrada_var.set(entrada_var.get()[:-1])

def calcular():
    expr = entrada_var.get().strip()
    if not expr:
        return
    try:
        resultado = eval(expr)
        entrada_var.set(str(resultado))
    except ZeroDivisionError:
        entrada_var.set("Erro divisão por 0")
    except Exception:
        entrada_var.set("Erro")

#Criação dos botões em looping
botoes = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 5, 0),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 5, 1),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 5, 2),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 6, 0),
]

for (texto, linha, coluna) in botoes:
    if texto == "=":
        botao = tk.Button(
            janela, text=texto,font=('Arial',16), width=5, height=2,
            command=calcular
        )
    else:
        botao = tk.Button(
            janela, text=texto,font= ("Arial",16), width=5, height=2,
            command=lambda t=texto: clicar(t)
        )

    botao.grid(row=linha, column=coluna, padx=2, pady=2)

#botão para apagar tudo
botao_c = tk.Button(janela, text='c', font=('bold', 16), command=limpar)
botao_c.grid(row=6, column=2, columnspan=2, padx=4, pady=4)

#botão para apagar último
botao_ultimo = tk.Button(janela, text='X', font=('bold', 16), command=backspace)
botao_ultimo.grid(row=6, column=1, columnspan=2, padx=4, pady=4)

#Faz as células da grade redimensionarem proporcionalmente
for i in range(6):
    janela.grid_rowconfigure(i, weight=1)
for j in range(4):
    janela.grid_columnconfigure(j, weight=1)

#Calculos utilizando teclado físico
def on_key(event):
    allowed = '0123456789,+-*/()%'
    if event.keysym == 'Return':  # tecla enter
        calcular()
        return "break"
    if event.keysym == 'Escape':  # tecla Esc
        limpar()
        return "break"
    if event.keysym == 'BackSpace':  # tecla BackSpace
        backspace()
        return "break"
    if event.char in allowed and event.char != "":  # numeros e operadores
        clicar(event.char)
        return "break"

    return "break"

#conecta o teclado á janela
entrada.bind('<KeyPress>', on_key)

#fechamento e ciclo do looping da calculadora visual
janela.mainloop()