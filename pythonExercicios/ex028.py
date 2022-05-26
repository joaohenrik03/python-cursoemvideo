from random import randint
from time import sleep
print('-=-=-=' * 8)
print('INICIO | Jogo de adivinhação v1.0')
print('-=-=-=' * 8)
numcomp = randint(0, 5)
print('Nosso robô pensou em um número de 0 a 5, adivinhe qual é!')
numusu = int(input('Digite o número: '))
print('Processando...')
sleep(2)
if numusu == numcomp:
    print('Parabéns! Você acertou e ganhou, realmente era o número {}, que cara sortudo!'.format(numusu))
else:
    print('Não foi dessa vez, o número era {}, você errou, tente novamente!'.format(numcomp))
print('-=-=-=' * 8)
print('FIM | Jogo de adivinhação v1.0')
print('-=-=-=' * 8)
