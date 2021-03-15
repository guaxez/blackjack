'''
Jogo de 21
'''

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


print('21')

a = Carta(1,'C')
print(a)
