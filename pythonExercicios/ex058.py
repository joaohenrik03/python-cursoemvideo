from random import randint
from time import sleep
print('-=-=-=' * 8)
print('INICIO | Jogo de adivinhação v2.0')
print('-=-=-=' * 8)

numComputador = randint(0, 10)
print('Nosso robô pensou em um número de 0 a 10, adivinhe qual é para ganhar o jogo!')

res = numComputador + 1
while res != numComputador:
    res = int(input('Digite o número: '))
    print('Processando...')
    sleep(1)
    if res != numComputador:
        print('Você errou, tente novamente até acertar!')

if res == numComputador:
    print('Parabéns! Você acertou e ganhou, realmente era o número {}, que cara sortudo!'.format(res))
print('-=-=-=' * 8)
print('FIM | Jogo de adivinhação v2.0')
print('-=-=-=' * 8)


