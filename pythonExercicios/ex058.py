# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
# necessários para vencer.

from random import randint
from time import sleep

print('-=-=-=' * 8)
print('INICIO | Jogo de adivinhação v2.0')
print('-=-=-=' * 8)

numComputador = randint(0, 10)
print('Nosso robô pensou em um número de 0 a 10, adivinhe qual é para ganhar o jogo!')

res = numComputador + 1
tentativas = 0
while res != numComputador:
    res = int(input('Digite o número: '))

    tentativas = tentativas + 1
    print('Processando...')
    sleep(1)

    if res != numComputador:
        print('Você errou, tente novamente até acertar!')

if res == numComputador:
    print('Parabéns! Você acertou depois de {} tentativas e ganhou!'.format(tentativas))
    print('Realmente era o número {}, que cara sortudo!'.format(res))

print('-=-=-=' * 8)
print('FIM | Jogo de adivinhação v2.0')
print('-=-=-=' * 8)
