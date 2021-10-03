# Robô comprador de Papel Higiênico
# acrescentada flexibilidade: compra depende do preço. 
# Mas se houver festa, viagem ou isitas ele comprada outras quantidades para se adequar

import tkinter as tkr
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random


class Ambiente: # ambiente
                               # parâmetros iniciais
    def __init__(self, estoque_inicial, cons_min, cons_max, cons_med, preco_min: float, preco_max: float,
                 preco_med: float):
        # gera estoque inicial e consumo
        self.estoque_inicial = estoque_inicial
        self.cons_min = cons_min
        self.cons_max = cons_max
        self.cons_med = cons_med

        self.preco_min = preco_min
        self.preco_max = preco_max
        self.preco_med = preco_med


        self.estoque = self.estoque_inicial
        self.visita_ = False
        self.festa_  = False
        self.viagem_ = False


    def preco_atual(self):                      # calcula preço atual do rolo de papel higiênico
        self.preco_atual_ = random.uniform(self.preco_min, self.preco_max)
        self.preco_agora = round(self.preco_atual_, 2)
        return self.preco_agora

    def estoque_atual(self, compra):        # confere estoque
        self.estoque += compra
        return self.estoque

    def acao(self):
        pass

    def gasto_semanal___(self):              # calcula quanto foi gasto de papel higiênico
        self.gasto_semanal = random.randint(self.cons_min, self.cons_max)
        self.estoque -= self.gasto_semanal
        return self.gasto_semanal




class Agente():
    def __init__(self):
        self.media_gasto = 10
        self.media_preco = 10
    # memória
        self.mem_gasto = [] # acumula os gastos das semana
        self.mem_preco = [] # acumula os precos das semana
        self.med_gast  = [1]
        self.med_prec  = [1]
        self.marcador_compra = 0


    def media_gastos__(self):  # media dos gastos de todas as semanas
        self.media_gasto = sum(self.mem_gasto) / len(self.mem_gasto)
        return self.media_gasto

    def media_precos__(self): # media de preços de todas as semanas
        self.media_preco = sum(self.mem_preco) / len(self.mem_preco)
        return self.media_preco

    def visita(self):
        x = random.randint(1, 100)
        if x < 30:
            self.visita_ = True
        else:
            self.visita_ = False
        print(x)

        return self.visita_

    def festa(self):
        x = random.randint(1, 100)
        if x < 30:
            self.festa_ = True
        else:
            self.festa_ = False

        print(x)

        return self.festa_

    def viagem(self):
        x = random.randint(1, 100)
        if x < 30:
            self.viagem_ = True
        else:
            self.viagem_ = False

        print(x)

        return self.viagem_

    def comprar(self,x,y):            # CRENÇA se está barato completa o estoque

        if x > 1.0:  # está caro             # CRENÇA se está caro, compra só o mínimo para não faltar
            z = 8 - y  # completa o estoque só até 8 unidades (consumo máximo) -- se for negativo passa z pra 0
            self.marcador_compra = 1
        if x <= 1.0:  # está barato
            z = 12 - y  # completa o estoque só até 12 unidades
            self.marcador_compra = 2



        if self.viagem_ == True and self.visita_ == False  and self.festa_ == False: # se houver somente viagem compra o minimo, independente do preço
            z = 8 - y
            self.marcador_compra = 3

        if self.visita_ == True: # se houver visita compra o máximo, independente do preço
            z = 12 - y
            self.marcador_compra = 4

        if self.festa_ == True: # se houver festa compra o máximo, independente do preço
            z = 12 - y
            self.marcador_compra = 5

        if self.festa_ == True and self.visita_ == True: # se houver festa e visita compra o máximo, independente do preço
            z = 12 - y
            self.marcador_compra = 6



        if z < 0:
            z = 0


        return z


    # recebe percepções do corpo
    # calcula a quantidade a ser comprada
    # envia comando ao corpo



        #    estoque, cons_min cons_max cons_med preço_min preço_max preço_med
amb = Ambiente(12,        2,        8,       5,     0.6,       1.4,     1.0)     # criando objeto Ambiente e definindo parâmetros

agt = Agente()                                # criando objeto agente

x1 = []
x2 = []
x3 = [2]
x4 = [2]


# informando previamente se vai haver visita, festa ou viagem
agt.visita()
agt.festa()
agt.viagem()



""" CRIANDO JANELA"""
janela = tkr.Tk()

""" EDITAR JANELA """
janela.title("Embedding in Tk")
janela.geometry("600x400")

""" CRIANDO GRÁFICO 1 """
fig = plt.Figure(figsize=(3, 2), dpi=50)
fig.add_subplot(111).plot(x1,agt.mem_gasto,"") # "bo" = exibe em bolinha

""" CRIANDO GRÁFICO 2 """
fig2 = plt.Figure(figsize=(3, 2), dpi=50)
fig2.add_subplot(111).plot(x2,agt.mem_preco,"") # "bo" = exibe em bolinha

""" CRIANDO GRÁFICO 3 """
fig3 = plt.Figure(figsize=(3, 2), dpi=50)
fig3.add_subplot(111).plot(x3,agt.med_gast, "") # "bo" = exibe em bolinha

""" CRIANDO GRÁFICO 4 """
fig4 = plt.Figure(figsize=(3, 2), dpi=50)
fig4.add_subplot(111).plot(x4,agt.med_prec, "") # "bo" = exibe em bolinha


""" CARREGANDO GRÁFICO 1 NO TKINTER """
chart = FigureCanvasTkAgg(fig,janela)
chart.get_tk_widget().grid(row=0,column=0)

""" CARREGANDO GRÁFICO 2 NO TKINTER """
chart2 = FigureCanvasTkAgg(fig2,janela)
chart2.get_tk_widget().grid(row=0,column=1)

""" CARREGANDO GRÁFICO 3 NO TKINTER """
chart3 = FigureCanvasTkAgg(fig3,janela)
chart3.get_tk_widget().grid(row=0,column=2)

""" CARREGANDO GRÁFICO 4 NO TKINTER """
chart4 = FigureCanvasTkAgg(fig4,janela)
chart4.get_tk_widget().grid(row=0,column=3)

global marcador_btn
marcador = 0

""" BOTÃO """

cont1 = -1
def bt_click():
    global cont1
    global marcador
    marcador += 1


    if marcador == 1:
        lb1["text"] = "<<<<<--->>>>>"
        lb2["text"] = "<<<<<--->>>>>"
        lb3["text"] = "<<<<<--->>>>>"
        lb4["text"] = "<<<<<--->>>>>"
        lb5["text"] = "<<<<<--->>>>>"
        lb6["text"] = "<<<<<--->>>>>"
        lb7["text"] = "*** Iniciar a semana? ***"

    elif marcador == 2:

        lb1["text"] = "                               *** A semana começou! ***"
        lb2["text"] = "<<<<<<<< Você tem os seguintes dados do ambiente >>>>>>>>"
        lb3["text"] = "Estoque de Papel: " + str(amb.estoque_inicial)
        lb4["text"] = "Consumo mínimo: "   + str(amb.cons_min) +  "   ---- Preço mínimo   : " + str(amb.preco_min)
        lb5["text"] = "Consumo Máximo: "   + str(amb.cons_max) +  "  ---- Preço máximo   : " + str(amb.preco_max)
        lb6["text"] = "Média de consumo: " + str(amb.cons_med) +  " ---- Média de preco : " + str(amb.preco_med)
        lb7["text"] = "*** Simular o gasto da semana? ***"

        marcador = 3

    elif marcador == 3:


        if agt.viagem_ == True:
            lb1["text"] = "Ôpa: temos viagem essa semana"
        else:
            lb1["text"] = "<<<<<--->>>>>"

        if agt.visita_ == True:
            lb2["text"] = "Ôpa: temos visitas essa semana"
        else:
            lb2["text"] = "<<<<<--->>>>>"

        if agt.festa_ == True:
            lb3["text"] = "Ôpa: temos festa essa semana"
        else:
            lb3["text"] = "<<<<<--->>>>>"



        lb4["text"] = "<<<<<--->>>>>"
        lb5["text"] = "<<<<<--->>>>>"
        lb6["text"] = "<<<<<--->>>>>"
        lb7["text"] = "*** Simular o gasto da semana? ***"


    elif marcador == 4:
        cont1 = cont1 + 1
        g = amb.gasto_semanal___()  # calcula quanto foi gasto de papel higiênico na semana / randômico
        agt.mem_gasto.append(g)  # memoriza gasto da semana
        x1.append(cont1)
        #agt.mem_gasto[cont1] = g
        e = amb.estoque
       #fig.add_subplot(111).plot(x1, agt.mem_gasto, "")  # "bo" = exibe em bolinha

        lb1["text"] = "<<<<<--->>>>>"
        lb2["text"] = "<<<<<--->>>>>"
        lb3["text"] = "<<<<<--->>>>>"
        lb4["text"] = "Rolos gastos na semana: " + str(g)
        lb5["text"] = "Em estoque: " + str(e)
        lb6["text"] = "<<<<<--->>>>>"
        lb7["text"] = "*** Deseja que o robô faça as compras? ***"

        agt.media_gastos__()
        agt.med_gast[0] = agt.media_gasto

        fig.add_subplot(111).plot(x1, agt.mem_gasto, "")  # "bo" = exibe em bolinha
        chart = FigureCanvasTkAgg(fig, janela)
        chart.get_tk_widget().grid(row=0, column=0)

        fig3.add_subplot(111).plot(x3, agt.med_gast, "")  # "bo" = exibe em bolinha
        chart3 = FigureCanvasTkAgg(fig3, janela)
        chart3.get_tk_widget().grid(row=0, column=2)

    elif marcador == 5:

        p = amb.preco_atual()  # calcula preço atual do rolo de papel higiênico / randômico
        agt.mem_preco.append(p)  # memoriza preco da semana
        #agt.mem_preco[cont1] = p
        x2.append(cont1)

        compra = agt.comprar(p, amb.estoque)
        e = amb.estoque_atual(compra)

        lb1["text"] = ">> Preço >>>> " + str(p)
        lb2["text"] = ">> Estoque >>> " + str(amb.estoque)
        lb3["text"] = "<<<<<--->>>>>"



        if agt.marcador_compra == 1:  # está caro
            lb4["text"] = "Estava muito caro!"
            lb5["text"] = "Comprei apenas o suficiente. Temos agora: " + str(e) + " unidades"

        if agt.marcador_compra == 2:  # está barato
            lb4["text"] = "Tava barato demais!!!"
            lb5["text"] = " Comprei bastante para completar o estoque! Temos agora: " + str(
                e) + " unidades"

        if agt.marcador_compra == 3:  # viagem
            lb4["text"] = "Temos viagem essa semana!!!"
            lb5["text"] = " Comprei apenas o suficiente! Temos agora: " + str(
                e) + " unidades"

        if agt.marcador_compra == 4:  # visita
            lb4["text"] = "Temos visita essa semana!!!"
            lb5["text"] = " Comprei bastante para completar o estoque! Temos agora: " + str(
                e) + " unidades"

        if agt.marcador_compra == 5:  # festa
            lb4["text"] = "Temos festa!!!"
            lb5["text"] = " Comprei bastante para completar o estoque! Temos agora: " + str(
                e) + " unidades"

        if agt.marcador_compra == 6:  # visita e festa
            lb4["text"] = "Temos visita e festa!!!"
            lb5["text"] = " Comprei bastante para completar o estoque! Temos agora: " + str(
                e) + " unidades"

        lb6["text"] = "<<<<<--->>>>>"
        lb7["text"] = "<<<<< Deseja simular outra semana? >>>>> "

        agt.media_precos__()
        agt.med_prec[0] = agt.media_preco

        fig2.add_subplot(111).plot(x2, agt.mem_preco, "")  # "bo" = exibe em bolinha
        chart2 = FigureCanvasTkAgg(fig2, janela)
        chart2.get_tk_widget().grid(row=0, column=1)

        fig4.add_subplot(111).plot(x4, agt.med_prec, "")  # "bo" = exibe em bolinha
        chart4 = FigureCanvasTkAgg(fig4, janela)
        chart4.get_tk_widget().grid(row=0, column=2)

        marcador = 2
        agt.visita()  # avisa se na próxima semana haverá festa, visitas ou viagem
        agt.festa()
        agt.viagem()



    else:
        pass






bt = Button(janela, width="20", text="ok", command=bt_click)
bt.place(x=175, y=370)


""" LABEL """
lb1 = Label(janela, text="                        Seja Bem-Vindo!")
lb1.place(x=130, y=220)

lb2 = Label(janela, text=" Eu sou o robô comprador de papel higiênico")
lb2.place(x=130, y=240)

lb3 = Label(janela, text="")
lb3.place(x=130, y=260)

lb4 = Label(janela, text="")
lb4.place(x=130, y=280)

lb5 = Label(janela, text="")
lb5.place(x=130, y=300)

lb6 = Label(janela, text="")
lb6.place(x=130, y=320)

lb7 = Label(janela, text="")
lb7.place(x=130, y=340)

tkr.mainloop()

