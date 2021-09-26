# primeira parte
# próxima parte = adicionar histórico em dicionários ou tuplas


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
        pass

    def comprar(self,x,y):            # CRENÇA se está barato completa o estoque
        if x > 1.0:  # está caro             # CRENÇA se está caro, compra só o mínimo para não faltar
            self.z = 8 - y  # completa o estoque só até 8 unidades (consumo máximo)

        if x <= 1.0:  # está barato
            self.z = 12 - y  # completa o estoque só até 12 unidades

            return self.z


    # recebe percepções do corpo
    # calcula a quantidade a ser comprada
    # envia comando ao corpo

        #    estoque, cons_min cons_max cons_med preço_min preço_max preço_med
amb = Ambiente(12,        2,        8,       5,     0.6,       1.0,     1.4)     # criando objeto Ambiente e definindo parâmetros

agt = Agente()                                # criando objeto agente

comeco = " "                # tela inicial mostra o estoque e consumo
while (comeco != "s"):
    comeco = input("Iniciar a semana? s/n: ")
    if comeco == "s" :
        print("A semana começou!", "\n <<<<<<<< Você tem os seguintes dados do ambiente >>>>>>>>",
              "\nEstoque de Papel:",amb.estoque_inicial,"\nConsumo mínimo:",amb.cons_min,"\nConsumo Máximo:",amb.cons_max,
              "\nMédia de consumo",amb.cons_med,"\nPreço mínimo:",amb.preco_min,"\npreço Máximo",amb.preco_max,
              "\nMédia de preço:",amb.preco_med,)
    if comeco == "n" :
        pass

retornar = " "               # loop para começar tudo de novo
while (retornar != "n"):     # loop para começar tudo de novo


    semana = " "                             #  gasto de papel da semana
    while (semana != "s"):
        semana = input("*** Simular o gasto da semana? *** s/n: ")
        if semana == "s" :
            g = amb.gasto_semanal___()
            e = amb.estoque
            print("Rolos gastos na semana:", g, "\nEm estoque:", e)

        if semana == "n" :
            pass


    compra = " "                         # robô faz a compra para abastecer o estoque
    while (compra != "s"):
        compra = input("Deseja que o robô faça as compras? s/n: ")
        if compra == "s" :
            p = amb.preco_atual()
            amb.estoque_atual(agt.comprar(p, amb.estoque))
            if p > 1.0:  # está caro
                print("Estava muito caro! -- Comprei apenas o suficiente")

            if p <= 1.0:  # está barato
                print("Tava barato demais!!! - comprei bastante para completar o estoque!")
        # ----------- While de retorno ----------------------------------------------
        # loop para retornar ou terminar
        retornar = input("Deseja simular outra semana?>>>>>> s/n: ")  # volta ao início

        if retornar == "s":
            pass
        if retornar == "n":
            pass
        #-------------------------------------------------------------------------



        if compra == "n" :
            pass





