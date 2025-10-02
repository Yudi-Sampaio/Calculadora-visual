# calculadora visual computador att1

import tkinter as tk
from tkinter import messagebox, simpledialog

# interface visual da calculadora
janela = tk.Tk()
janela.title("Calculadora Visual")
janela.geometry("350x480")
janela.resizable(False, False)

# campo de texto
entrada_var = tk.StringVar()
entrada = tk.Entry(janela, textvariable=entrada_var, width=20, font=('bold', 50), justify="left", bg="#34495e",
                   fg="white", insertbackground="white")
entrada.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
entrada.focus_set()
entrada.pack(fill="both", padx=10, pady=10)

# frame dos botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack()

# Criação do historico
historico = []


def salvar_calculo(expressao, resultado):
    historico.append({"expressao": expressao, "resultado": resultado})

#arquivo historico calculadora
    with open ("historico_calculadora.txt", "a")as hc:
        hc.write (f"{expressao} = {resultado}\n")

#continuação historico
def listar_historico():
    try:
        with open("historico_calculadora.txt" , "r") as hc:
            linhas = hc.readlines()
    except FileNotFoundError:
        messagebox.showinfo("historico", "Nenhum cálculo salvo")
        return
    if not linhas:
        messagebox.showinfo("Histórico", "Nenhum cálculo salvo")
        return
    texto = ""
    for i,linha in enumerate (linhas,start = 1):
        texto += f"{i}. {linha}"

    messagebox.showinfo("Historico", texto)


def atualizar_calculo():
    with open ("historico_calculadora.txt", "r") as hc:
        linhas = hc.readlines()
    if not linhas:
        messagebox.showwarning("Atualizar", "Nenhum cálculos para atualizar.")
        return
    listar_historico()
    indice = simpledialog.askinteger("Atualizar", "Número do cálculo para atualizar.") - 1
    if 0 <= indice < len(linhas):
        nova_expr = simpledialog.askstring("Atualizar", "Nova expressao:")
        try:
            novo_result = eval(nova_expr)
            linhas[indice] = f"{nova_expr} = {novo_result}\n"
            with open("historico_calculadora.txt", "w") as hc:
                hc.writelines (linhas)
            messagebox.showinfo("Atualizar", "Cálculo atualizado com sucesso!")
        except:
            messagebox.showerror("Erro", "Expressao inválida!")
    else:
        messagebox.showwarning("Erro", "Cálculo nao encontrado.")


def deletar_calculo():
    with open ("historico_calculadora.txt", "r") as hc:
        linhas = hc.readlines()
    if not linhas:
        messagebox.showwarning("Deletar", "Nenhum calculo para deletar")
        return
    listar_historico()
    indice = simpledialog.askinteger("Deletar", "Numero do cálculo a deletar") - 1
    if 0 <= indice < len(linhas):
        removido = linhas.pop(indice)
        with open ("historico_calculadora.txt", "w") as hc:
            hc.writelines(linhas)
        messagebox.showinfo("Deletar", f"cálculo{removido} deletado!")
    else:
        messagebox.showwarning("Erro", "Cálculo não encontrado")


# botões de interação
def clicar(valor):
    entrada.insert(tk.END, str(valor))


def limpar():
    entrada.delete(0, tk.END)


def backspace():
    entrada_var.set(entrada_var.get()[:-1])


def calcular():
    expressao = entrada_var.get().strip()
    if not expressao:
        return
    try:
        resultado = eval(expressao)
        entrada_var.set(str(resultado))
        salvar_calculo(expressao, resultado)
    except ZeroDivisionError:
        entrada_var.set("Erro divisão por 0")
    except Exception:
        entrada_var.set("Erro")


#Criação dos botões em looping

botoes = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3),
]

for (texto, linha, coluna) in botoes:
    if texto == "=":
        botao = tk.Button(
            frame_botoes, text=texto, width=5, height=2,
            command=calcular, font=("Arial", 12)
        )
    else:
        botao = tk.Button(
            frame_botoes, text=texto, width=5, height=2, font=("Arial", 12),
            command=lambda t=texto: clicar(t)
        )

    botao.grid(row=linha, column=coluna, padx=5, pady=5)

# botão para apagar tudo
botao_c = tk.Button(frame_botoes, text='c', font=('bold', 16), command=limpar)
botao_c.grid(row=0, column=4, columnspan=2, padx=4, pady=4)

# botão para apagar último
botao_ultimo = tk.Button(frame_botoes, text='X', font=('bold', 16), command=backspace)
botao_ultimo.grid(row=1, column=4, columnspan=2, padx=4, pady=4)

# botõees CRUD do historico
frame_historico = tk.Frame(janela)
frame_historico.pack(pady=10)

tk.Button(frame_historico, text="Ver Historico", width=20,
          command=listar_historico).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_historico, text="Atualizar Historico", width=20,
          command=atualizar_calculo).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame_historico, text="Deletar do Historico", width=20,
          command=deletar_calculo).grid(row=2, column=0, padx=5, pady=5)

# Faz as células da grade redimensionarem proporcionalmente
for i in range(6):
    janela.grid_rowconfigure(i, weight=1)
for j in range(4):
    janela.grid_columnconfigure(j, weight=1)


# Calculos utilizando teclado físico
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


# conecta o teclado á janela
entrada.bind('<KeyPress>', on_key)

# fechamento e ciclo do looping da calculadora visual
janela.mainloop()
