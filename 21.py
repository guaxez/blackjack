'''
Jogo de 21
'''

class Carta():

    def __init__(self, num, tipo):
        self.numero = num
        self.naipe = tipo

    def __str__(self):
        return '{}{}'.format(self.numero,self.naipe)


print('21')

a = Carta(1,'C')
print(a)
