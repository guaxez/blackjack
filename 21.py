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
    
    def dar_carta(self,quem,quantas=1):
        for cartas in range(quantas):
            quem.mao.append(self.pilha[-1])
            self.pilha.pop()
            quem.valor = quem.valor_mao()
            print(self.tamanho_baralho())
            if quem.valor > 21:
                quem.rodada = 'estourou'
    
    def rodada(self,participantes):
        quant = len(participantes)
        participantes[1].apostar()
        print('Dar cartas')
        self.dar_carta(participantes[0])
        self.dar_carta(participantes[1],2)
        print('Banca: [{}]: {}'.format(participantes[0].mao[0],participantes[0].valor))
        print('Jogador: {}: {}'.format(participantes[1].mao,participantes[1].valor))
        opcao = input('1-Carta/2-Ficar:')
        while opcao == '1':
            self.dar_carta(participantes[1])
            print('Jogador: {}: {}'.format(participantes[1].mao,participantes[1].valor))
            opcao = input('1-Carta/2-Ficar:')
            if opcao == '2':
                break
        while participantes[0].valor < 17:
            self.dar_carta(participantes[0])
        print('Banca: [{}]: {}'.format(participantes[0].mao,participantes[0].valor))
        if participantes[0].valor_mao() > participantes[1].valor_mao() or participantes[1].rodada == 'estourou':
            print('Banca vence!')
            participantes[1].reset_rodada()
            participantes[0].reset_rodada()
        elif participantes[0].valor_mao() < participantes[1].valor_mao():
            print('Jogador vence!')
            participantes[1].dinheiro += participantes[1].aposta * 2
            participantes[1].reset_rodada()
            participantes[0].reset_rodada()
        else:
            print('Push')
            participantes[1].dinheiro += participantes[1].aposta
            participantes[1].reset_rodada()
            participantes[0].reset_rodada()
        
        

class Jogador():

    def __init__(self,nome,dinheiro):
        self.nome = nome
        self.mao = []
        self.dinheiro = dinheiro
        self.aposta = 0
        self.valor = 0
        self.rodada = 'jogando'
    
    def status(self):
        print('{} $:{} AP:{} M:{} V:{}'.format(self.nome, self.dinheiro, self.aposta, self.mao,self.valor))
    
    def mostra_mao(self): # agora que eu mudei o __str__ das cartas para __repr__, acho que nao preciso mais disso. mas vou deixar por enquanto
        for c in self.mao: #talvez essa função ainda seja util, se eu arrumar ela. Como uma versão da func status. Mostrar x cartas e o valor delas.
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
    
    def reset_rodada(self):
        self.aposta = 0
        self.mao = []
        self.valor = 0
        self.rodada = 'jogando'



# MAIN

print('21')
bar = Baralho()
bar.embaralhar()
print(bar.tamanho_baralho())

banca = Jogador('Banca',999999)
banca.status()
jogador = Jogador('Jogador',500)
jogador.status()

bar.rodada([banca,jogador])
jogador.status()
banca.status()
