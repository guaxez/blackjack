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
        self.numero = num
        self.naipe = tipo
        self.st_num = self.tipos[str(num)]
        self.st_tipo = self.tipos[str(tipo)]

    def __repr__(self):
        return '{} de {}'.format(self.st_num,self.st_tipo)

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
        return 'tamanho do baralho: {}'.format(len(self.pilha))
    
    def dar_carta(self,quem):
        quem.mao.append(self.pilha[-1])
        self.pilha.pop()
        quem.valor = quem.valor_mao()
        print(self.tamanho_baralho())
        quem.status()
    
    def rodada(self,participantes):
        quant = len(participantes)
        participantes[1].apostar()
        print('Dar cartas')
        for quem in participantes:
            self.dar_carta(quem)
            self.dar_carta(quem)
        if participantes[0].valor_mao() > participantes[1].valor_mao():
            print('Banca vence!')
            participantes[1].aposta = 0
        elif participantes[0].valor_mao() < participantes[1].valor_mao():
            print('Jogador vence!')
            participantes[1].dinheiro += participantes[1].aposta * 2
            participantes[1].aposta = 0
        else:
            print('Push')
            participantes[1].dinheiro += participantes[1].aposta
            participantes[1].aposta = 0
        


class Jogador():

    def __init__(self,nome):
        self.nome = nome
        self.mao = []
        self.dinheiro = 500
        self.aposta = 0
        self.valor = 0
        self.rodada = 'jogando'
    
    def status(self):
        print('{} $:{} AP:{} M:{} V:{}'.format(self.nome, self.dinheiro, self.aposta, self.mao,self.valor))
    
    def mostra_mao(self): # agora que eu mudei o __str__ das cartas para __repr__, acho que nao preciso mais disso. mas vou deixar por enquanto
        for c in self.mao:
            print(c)
        print(self.valor_mao())
        
    
    def valor_mao(self):
        valor = 0
        for c in self.mao:
            if c.numero >= 10:
                valor += 10
            elif c.numero > 1 and c.numero < 10:
                valor += int(c.numero)
            else:
                valor += 11 # o ás pode ser 1 ou 11, tenho que resolver isso. Acho melhor desenvolver a aposta antes.
        return valor
    
    def apostar(self,valor=10):
        self.dinheiro -= valor
        self.aposta += valor
        return valor



# MAIN

print('21')
bar = Baralho()
bar.embaralhar()
print(bar.tamanho_baralho())

banca = Jogador('Banca')
banca.status()
jogador = Jogador('Jogador')
jogador.status()

bar.rodada([banca,jogador])
jogador.status()
