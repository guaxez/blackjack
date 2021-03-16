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
    
    def tamanho_baralho(self):
        return 'tamanho do baralho: {}'.format(len(b.pilha))
    
    def dar_carta(self,quem):
        quem.mao.append(self.pilha[-1])
        self.pilha.pop()
        print(self.tamanho_baralho())
        quem.status()

class Jogador():

    def __init__(self,nome):
        self.nome = nome
        self.mao = []
        self.dinheiro = 500
    
    def mostra_mao(self):
        for c in self.mao:
            print(c)


    def status(self):
        print('{} {} {}'.format(self.nome, self.dinheiro, self.mao))



# MAIN

print('21')
b = Baralho()
b.embaralhar()
print(b.tamanho_baralho())

jogador = Jogador('Jogador')
jogador.status()

b.dar_carta(jogador)
jogador.mostra_mao()
