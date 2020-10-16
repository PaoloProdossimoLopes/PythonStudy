#importar a biblioteca que gera numeros randomicamente
import random
#Importar o gerador de interfacie basica
import PySimpleGUI as sg


class SimuladorDeDados:

    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        #layout
        self.layout = [
            [sg.text('Jogar o dado?')]
            [sg.button('Sim'), sg.button('Não')]
        ]
        

    def Iniciar(self):
        self.janela = sg.window('Simulador de dado', Layout = self.layout)
        #Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        #Fazer alguma ação com esses valores
        try:
            if self.eventos == 'Sim':
                self.gerarValorDoDado()
            elif self.eventos == 'Não':
                print('Agracemos sua participação')
            else:
                print('Favor digitar Simou Não')
                #reiniciar o programa
        except:
            print('Ocorreu um erro ao receber sua resposta')
        
    def gerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

#Instanciando       
simulador = SimuladorDeDados()
simulador.Iniciar()

