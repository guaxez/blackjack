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

    def __init__(self,num_decks=1):
        self.pilha = []
        
        for i in range(num_decks):
            for j in ('O','E','C','P'):
                for k in range(1,14):
                    self.pilha.append(Carta(k,j))
        
        self.embaralhar()
    
    def mostrar_baralho(self):
        for k in self.pilha:
            print(k)
    
    def embaralhar(self):
        random.shuffle(self.pilha)
    
    def tamanho_baralho(self):
        return '{}'.format(len(self.pilha))
    
    def dar_carta(self,quem,quantas=1):
        for cartas in range(quantas):
            quem.mao.append(self.pilha[-1])
            self.pilha.pop()

            quem.valor = quem.valor_mao()
            if quem.valor > 21:
                quem.rodada = 'estourou'
            elif quem.valor == 21:
                quem.rodada = 'blackjack'
            print(quem.nome,quem.valor,quem.rodada,quem.mao)

            print(self.tamanho_baralho(),'cartas')
    
    def vencedor(self, jogadores):
        if jogadores[0].valor > 21:
            if jogadores[1].valor > 21:
                return('ESTOUROU')
            elif jogadores[1].valor <= 21:
                jogadores[1].dinheiro += jogadores[1].aposta
                return('VITÓRIA')
        if jogadores[1].valor > 21:
            return('ESTOUROU')
        elif jogadores[0].valor == jogadores[1].valor:
            jogadores[1].dinheiro += jogadores[1].aposta
            return('PUSH')
        elif jogadores[0].valor < jogadores[1].valor:
            jogadores[1].dinheiro += jogadores[1].aposta * 2
            return('VITÓRIA')
        else:
            return('BANCA VENCE')
    
    def jogoTerminal(self,participantes):
        quant = len(participantes)
        print('*'*30)

        apostei = input('Valor da aposta(int/x-sair): ')
        if apostei == 'x':
            print('Volte Sempre!')
            return
        while apostei != 'x':
            participantes[1].apostar(int(apostei)) # falta verificar se o valor de entrada é válido.

            print('*'*30)

            print('Dar cartas iniciais')
            self.dar_carta(participantes[0])
            self.dar_carta(participantes[1],2)
            print('Banca: {}: [{}]'.format(participantes[0].valor,participantes[0].mao[0]))
            print('Jogador: {} {}: {}'.format(participantes[1].valor,participantes[1].rodada,participantes[1].mao))

            print('-'*30)

            print('Cartas do jogador')

            
            while participantes[1].valor < 21:
                opcao = input('1-Carta/2-Ficar: ')
                if opcao == '2' or (participantes[1].valor > 21):
                    break
                elif opcao == '1':
                    self.dar_carta(participantes[1])
                
            
            print('-'*30)
            
            print('Cartas da Banca')

            if participantes[1].rodada == 'estourou':
                self.dar_carta(participantes[0])
            else:
                while participantes[0].valor < 17:
                    self.dar_carta(participantes[0])
            
            print('Banca: {} | Jogador: {}'.format(participantes[0].valor,participantes[1].valor))
            # BUG: Banca 21 e jogador > 21 e jogador vence
            # BUG: Dois bust e jogador vence
            # BUG: Duplo blackjack não dá push instantâneo
            # Bem eu claramente preciso revisar o esquema de win condition. Mudei bastante será que deu? Preciso testar.
            
            print(self.vencedor(participantes))

            participantes[0].reset_rodada()
            participantes[1].reset_rodada()
            participantes[1].status()

            if len(self.pilha) <= 52: # não consigo fazer 'if len(self.pilha) <= (len(self.pilha) / 2)'
                print('Iniciando novo baralho.')
                self.pilha = []
                self.__init__(2)
                print(self.tamanho_baralho(),'cartas')

            print('*'*30)

            apostei = input('Valor da aposta(int/x-sair): ')
        print('Volte Sempre!')
        
        
class Jogador():

    def __init__(self,nome,dinheiro):
        self.nome = nome
        self.mao = []
        self.dinheiro = dinheiro
        self.aposta = 0
        self.valor = 0
        self.rodada = 'jogando'
    
    def __repr__(self):
        return self.nome
    
    def status(self):
        print('{} $:{} AP:{} M:{} V:{}'.format(self.nome, self.dinheiro, self.aposta, self.mao,self.valor))
    
    def mostra_mao(self): # agora que eu mudei o __str__ das cartas para __repr__, acho que nao preciso mais disso. mas vou deixar por enquanto
        for c in self.mao: # talvez essa função ainda seja util, se eu arrumar ela. Como uma versão da func status. Mostrar x cartas e o valor delas.
            print(c)
        print(self.valor_mao())
        
    
    def valor_mao(self):
        valor = 0
        qtd_as = 0

        for c in self.mao:
            if c.numero >= 10:
                valor += 10
            elif c.numero > 1 and c.numero < 10:
                valor += c.numero
            else:
                qtd_as += 1

        for a in range(qtd_as):
            if valor < 11 and (valor + qtd_as < 21):
                valor += 11  # Ainda acho que falta algo no algoritmo, por exemplo se você comprar o ás na primeira carta mas
            else:            # você compra mais cartas. Como seria possível mudar o valor de um ás no começo da mão?
                valor += 1   # Tentei arrumar isso agora a pouco, mas acabei quebrando o código, e nem sabia como arrumar.
                             # Acho que consgui arrumar. Vou fazer uns testes.
                             # Comprei um oito um dois e dois ás e deu 22.O primeiro ás Devia virar 1 antes de estourar. Nem sei mais se essa porra ta arrumada ou não      
        if (valor == 21):
            self.rodada = 'blackjack'

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




if __name__ == '__main__':
    print('21 - Blackjack')

    bar = Baralho(2)
    print(bar.tamanho_baralho(),'cartas')

    banca = Jogador('Banca',999999)
    jogador = Jogador('Jogador',500)
    jogador.status()

    bar.jogoTerminal([banca,jogador])
