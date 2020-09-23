import tkinter as tk
from functools import partial
import random

# JOGO
def tente(botao):
    # ESCOLHA DO COMPUTADOR
    global lb_computador
    global lb_vencedor
    lb_computador.destroy()
    lb_vencedor.destroy()
    escolha_computador = opcoes[random.randint(0, 2)]
    # IMPRIMINDO NO SISTEMA ESCOLHA DO USUÁRIO E MOSTRANDO NA TELA
    escolha_usuario = str(ed.get()).strip().lower()
    if escolha_usuario == "pedra":
        escolha_usuario = opcoes[0]
        lb_pedra = tk.Label(janela, text="VOCÊ JOGOU PEDRA", bg="dark green")
        lb_pedra.place(x=140, y=150)
    elif escolha_usuario == "papel":
        escolha_usuario = opcoes[1]
        lb_papel = tk.Label(janela, text="VOCÊ JOGOU PAPEL", bg="dark green")
        lb_papel.place(x=140, y=150)
    elif escolha_usuario == "tesoura":
        escolha_usuario = opcoes[2]
        lb_tesoura = tk.Label(janela, text="VOCÊ JOGOU TESOURA", bg="dark green")
        lb_tesoura.place(x=140, y=150)
    else:
        lb_error = tk.Label(janela, text="OPÇÃO INVÁLIDA", bg="dark green")
        lb_error.place(x=140, y=150)
    # MOSTRANDO A JOGADA DO COMPUTADOR
    texto_computador = f"O COMPUTADOR JOGOU {escolha_computador.upper()}"
    lb_computador = tk.Label(janela, text=texto_computador, bg="dark green")
    lb_computador.place(x=110, y=190)
    # TESTE LÓGICO
    if escolha_usuario == "Pedra":
        if escolha_computador == "Pedra":
            vencedor = "ninguém"
        elif escolha_computador == "Papel":
            vencedor = "computador"
        elif escolha_computador == "Tesoura":
            vencedor = "você"
    elif escolha_usuario == "Papel":
        if escolha_computador == "Pedra":
            vencedor = "você"
        elif escolha_computador == "Papel":
            vencedor = "ninguém"
        elif escolha_computador == "Tesoura":
            vencedor = "computador"
    elif escolha_usuario == "Tesoura":
        if escolha_computador == "Pedra":
            vencedor = "computador"
        elif escolha_computador == "Papel":
            vencedor = "você"
        elif escolha_computador == "Tesoura":
            vencedor = "ninguém"
    # VENCEDOR
    texto_vencedor = f"O VENCEDOR É {vencedor.upper()}"
    lb_vencedor = tk.Label(janela, text=texto_vencedor, bg="dark green")
    lb_vencedor.place(x=120, y = 300)
# OPÇÕES
opcoes = ["Pedra", "Papel", "Tesoura"]
# INICIALIZAÇÃO JANELA
janela = tk.Tk()
janela.title("JO KEN PO!")
# LABEL 1
lb = tk.Label(janela, text="Digite aqui:", bg="dark green")
lb.place(x=160,y=50)
# MIGUÉ NAS LABELS
lb_computador = tk.Label(janela)
lb_computador.place(x=0,y=0)
lb_computador["bg"] = "green"
lb_vencedor = tk.Label(janela)
lb_vencedor.place(x=0,y=0)
lb_vencedor["bg"] = "green"
# ESCREVA
ed = tk.Entry(janela, width= 20)
ed.place(x=130,y=80)
# BOTÃO
bt1 = tk.Button(janela, width=20, text="JOGAR")
bt1.place(x=120, y=110)
bt1["command"] = partial(tente, bt1)
# PARTE TÉCNICA JANELA
janela.geometry("400x400+600+150")
janela['bg'] = "green"
janela.mainloop()
