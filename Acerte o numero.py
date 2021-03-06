# Projeto - Acerte o Numero: Programa para acertar o numero
# 

import random
import PySimpleGUI as sg

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 5
        self.tentar_novamente = True
    
    def Iniciar(self):
        # Layout
        layout = [
            [sg.Text('Seu Chute',size=(39,0))],
            [sg.Input(size=(18,0),key='ValorChute')],
            [sg.Button('Chutar!'), sg.Button('Sair')],
            [sg.Output(size=(39,10))]
        ]
        # criar uma janela
        self.janela = sg.Window('Chute o numero!',layout=layout, enable_close_attempted_event=True, finalize=True)
        self.GerarNumeroAleatorio()
        try:
            while True:
                # receber os valores
                self.evento, self.valores = self.janela.Read()
                # Fazer alguma coisa com estes valores
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor mais baixo!')
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um valor mais alto!')
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('PARABÉNS VOCÊ ACERTOU!!')
                elif self.evento == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
                    if sg.popup_yes_no('Do yuou really want to exit?') == 'Yes':
                        break
                if self.evento in (sg.WIN_CLOSED, 'Sair'):
                    break         
                                                                 
        except:
            if self.valores['ValorChute'] != int:
                print('Favor digitar apenas números!')
                self.Iniciar()
            
    def GerarNumeroAleatorio(self):
        self.valor_aleatorio =  random.randint(self.valor_minimo,self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()
window.close()
