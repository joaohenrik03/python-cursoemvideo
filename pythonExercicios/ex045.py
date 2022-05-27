# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

player = int(input('''\033[34mQual você deseja jogar? 
\033[35m[1] \033[97mPedra
\033[35m[2] \033[97mPapel
\033[35m[3] \033[97mTesoura
\033[34mOPÇÃO: '''))

print('\033[33m-=-=-=-=' * 5)
print('\033[97mPedra')
sleep(1)
print('Papel')
sleep(1)
print('Tesoura!!!\033[m')

pc = randint(1, 3)
if player == 1:
    if pc == 1:
        resultado = 'houve um EMPATE!'
        escolhaPc = 'Pedra'
        print('\033[32mO computador escolheu {}, {}!'.format(escolhaPc, resultado))
    elif pc == 2:
        resultado = 'você PERDEU'
        escolhaPc = 'Papel'
        print('\033[32mO computador escolheu {}, {}!'.format(escolhaPc, resultado))
    else:
        resultado = 'você GANHOU'
        escolhaPc = 'Tesoura'
        print('\033[32mO computador escolheu {}, {}!'.format(escolhaPc, resultado))
elif player == 2:
    if pc == 1:
        resultado = 'você GANHOU'
        escolhaPc = 'Pedra'
        print('\033[32mO computador escolheu {}, {}!'.format(escolhaPc, resultado))
    elif pc == 2:
        resultado = 'houve um EMPATE'
        escolhaPc = 'Papel'
        print('\033[32mO computador escolheu {}, {}!'.format(escolhaPc, resultado))
    else:
        resultado = 'você PERDEU'
        escolhaPc = 'Tesoura'
        print('\033[32mO computador escolheu {}, {}!'.format(escolhaPc, resultado))
elif player == 3:
    if pc == 1:
        resultado = 'você PERDEU'
        escolhaPc = 'Pedra'
        print('\033[32mO computador escolheu {}, {}!'.format(escolhaPc, resultado))
    elif pc == 2:
        resultado = 'você GANHOU'
        escolhaPc = 'Papel'
        print('\033[32mO computador escolheu {}, {}!'.format(escolhaPc, resultado))
    else:
        resultado = 'houve um EMPATE'
        escolhaPc = 'Tesoura'
        print('\033[32mO computador escolheu {}, {}!'.format(escolhaPc, resultado))
else:
    print('\033[31m[ERRO] insira uma opção válida e tente novamente.')
print('\033[33m-=-=-=-=' * 5)
