'''
Jogo de 21
'''
import random

class Carta():

    tipos = {
        '1':'Ás',
        '2':'Dois',
        '3':'Três',
        '4':'Quatro',
        '5':'Cinco',
        '6':'Seis',
        '7':'Sete',
        '8':'Oito',
        '9':'Nove',
        '10':'Dez',
        '11':'Valete',
        '12':'Dama',
        '13':'Rei',
        'O':'Ouros',
        'E':'Espadas',
        'C':'Copas',
        'P':'Paus'
    }


    def __init__(self, num, tipo):
        self.numero = self.tipos[str(num)]
        self.naipe = self.tipos[str(tipo)]

    def __str__(self):
        return '{} de {}'.format(self.numero,self.naipe)

class Baralho():

    def __init__(self):
        self.pilha = []
        
        for i in ('O','E','C','P'):
            for j in range(1,14):
                self.pilha.append(Carta(j,i))
    
    def mostrar_baralho(self):
        for k in self.pilha:
            print(k)
    
    def embaralhar(self):
        random.shuffle(self.pilha)
    
    def dar_carta(self,quem):
        quem.mao.append(self.pilha.pop())

class Jogador():

    def __init__(self):
        self.mao = []
        self.dinheiro = 500





# MAIN

print('21')
b = Baralho()
print('tamanho do baralho: {}'.format(len(b.pilha)))

jogador = Jogador()
print(jogador.dinheiro,jogador.mao)


print