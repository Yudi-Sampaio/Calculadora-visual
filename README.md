<div align="center">
<img width="236" height="431" alt="Captura de tela 2025-10-02 183724" src="https://github.com/user-attachments/assets/5461e14a-ea40-40be-a103-37ad8dca54d3" />
</div>


# Calculadora visual (Simples)
## Descrição

Calculadora visual simples, desenvolvida em python utilizando a biblioteca Tkinter,permitindo o uso da qual para fazer operações matematicas,contando com historico permanente, visual, atualizavel e deletavel.

## Requisitos
1. Precisa ter o Python instalado no cmd do computador
2. De preferencia estar com o python ou pycharm atualizado
3. usa-se a biblioteca tkinter mas ela já é instalada automaticamente com o python então nao precisa do comando para instala-la

## Gerar executavel
1. baixe o codigo da calculadora
2. vá no terminal do pycharm
3. digite pip install pyinstaller
4. digite: pyinstaller --onefile 

## Instrução de uso

Caso tenha o python instalado no cmd do computador basta apenas baixar e abrir o (.exe) da calculadora visual,calculadora tem a opção de atualizar,deletar e ver historico, mesmo abrindo e fechando o executal da interface as informações do historico continuam salvas,caso queira as limpalas use a opção deletar historico, bote qual o numero do historico que deseja deletar e digite na janela que irá aparecer após apertar deletar historico.

## Como funciona o codigo da calculadora

responsavel pela definição retorno e funcionamento do historico
```python
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
```
Responsavel pela interação e calculo dos botões visuais da calculadora
```python
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
```

# Licença MIT
The MIT License (MIT)

Copyright (c) 2025 Yudi Sampaio (Yudi Sampaio), https://github.com/Yudi-Sampaio

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


