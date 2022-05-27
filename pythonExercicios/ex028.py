# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print('-=-=-=' * 8)
print('INICIO | Jogo de adivinhação v1.0')
print('-=-=-=' * 8)

numComputador = randint(0, 5)
print('Nosso robô pensou em um número de 0 a 5, adivinhe qual é!')
numUsuario = int(input('Digite o número: '))
print('Processando...')
sleep(2)

if numUsuario == numComputador:
    print('Parabéns! Você acertou e ganhou, realmente era o número {}, que cara sortudo!'.format(numUsuario))
else:
    print('Não foi dessa vez, o número era {}, você errou, tente novamente!'.format(numComputador))

print('-=-=-=' * 8)
print('FIM | Jogo de adivinhação v1.0')
print('-=-=-=' * 8)
