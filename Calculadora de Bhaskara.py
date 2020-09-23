from tkinter import *
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

#ERRO
def error():
    janela2 = Tk()
    janela2.title("ERRO!")
    janela2["bg"] = "white"
    label_erro = Label(janela2, text="VOCÊ DIGITOU ALGO INVÁLIDO, TENTE NOVAMENTE", foreground="red", background="white")
    label_erro.grid(row=1, column=1, padx=20, pady=20)
    botao_erro = Button(janela2, text="OKAY")
    botao_erro.grid(row=2, column=1, pady=20)
    botao_erro["command"] = janela2.destroy
    janela2.geometry("+300+350")
    janela2.mainloop()

#RESOLUÇÃO DE BHASKARA
def button_click():
    a = digitar1.get()
    b = digitar2.get()
    c = digitar3.get()

    #VERIFICAÇÃO SE SÃO NÚMEROS OS DADOS COLETADOS
    if a.isnumeric() and b.isnumeric() and c.isnumeric():
        a = float(a)
        b = float(b)
        c = float(c)
        delta = (b**2) - (4*a*c)
        #RESOLUÇÃO
        try:
            lista = list()
            lista_2 = list()
            x1 = (-b+ sqrt(delta)) / (2 * a)
            x2 = (-b + (-sqrt(delta))) / (2 * a)
            resposta["text"] = f"X1 = {x1:.2f}\nX2 = {x2:.2f}"
            resposta.grid(row=6, column=2, pady=20)
            fig = plt.figure(figsize=(8, 4))
            arr = np.arange(-1000, 1000)
            for i in arr:
                y = a*(i**2) + b*i + c
                lista.append(y)
            for j in arr:
                y_2 = 2*a*j + b
                lista_2.append(y_2)
            ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.7])
            ax1.set_xlabel("X")
            ax1.set_ylabel("y")
            ax2 = fig.add_axes([0.3, 0.5, 0.1, 0.2])
            ax2.set_title("DERIVADA PRÓXIMO DE 0")
            ax1.set_title("GRÁFICO DA FUNÇÃO")
            ax2.set_ylim([-50, 50])
            ax2.set_xlim([-10, 10])
            ax1.plot(arr, lista, "r")
            ax2.plot(arr, lista_2, "b")
            plt.show()
        except ValueError:
            delta_negativo = f"({-delta})i"
            x1 = (-b) / (2 * a)
            resposta["text"] = f"X1 = {x1:.2f} + √{delta_negativo}/{2*a}\nX2 = {x1:.2f} - √{delta_negativo}/{2*a}"
            resposta.grid(row=6, column=2, pady=20)
        except ZeroDivisionError:
            error()
    else:
        error()



#JANELA DA CALCULADORA
janela = Tk()
janela.title("CALCULADORA")

#INFORMAÇÕES
titulo = Label(janela, text="CALCULADORA", bg="cyan")
titulo.grid(column=2, row=1, padx=50, pady=10)

exemplo = Label(janela, text="COLOQUE OS DADOS DA SEGUINTE FORMA:\n\nY = A²x + Bx + C", bg="cyan")
exemplo.grid(column=2, row=2, padx=10, pady=20)

valor1 = Label(janela, text="A", bg="cyan")
valor1.grid(column=1, row=3, padx=10, pady=40)

valor2 = Label(janela, text="B", bg="cyan")
valor2.grid(column=2, row=3, padx=10)

valor3 = Label(janela, text="C", bg="cyan")
valor3.grid(column=3, row=3, padx=10)

#COLETA DE DADOS
digitar1 = Entry(janela)
digitar1.grid(column=1, row=4, padx= 10)

digitar2 = Entry(janela)
digitar2.grid(column=2, row=4, padx=10)

digitar3 = Entry(janela)
digitar3.grid(column=3, row=4, padx=10)

coletar = Button(janela, text="RESOLVER", command=button_click)
coletar.grid(column=2, row=5, pady=30)

#LABEL DA RESPOSTA
resposta = Label(janela, foreground="black", background="cyan")

#JANELA PARTE TÉCNICA
janela.resizable(width=False, height=False)
janela["bg"] = "white"
janela.geometry("550x450+200+150")
janela.mainloop()
