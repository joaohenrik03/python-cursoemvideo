#  Faça um programa que jogue par ou ímpar com o computador.
#  O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou
#  no final do jogo.

import random
import time

numPc = numJogador = jogosGanhos = 0
while True:
    print('-=-' * 15)
    numPc = random.randint(1, 2)
    escolha = str(input('Par ou ímpar [P/I]: '))

    if escolha.upper() != 'P' and escolha.upper() != 'I':
        print('[Erro], escolha inválida, o programa será encerrado!')
        break

    print('Vai começar!')
    time.sleep(1)
    print('Par...')
    time.sleep(1)
    print('ou...')
    time.sleep(1)
    print('Ímpar!')

    numJogador = int(input('Diga um valor: '))

    res = (numPc + numJogador) % 2

    print('-=-' * 15)
    if escolha.upper() == 'P':
        if res == 0:
            jogosGanhos += 1
            print(f'Você jogou {numJogador} e seu adversário jogou {numPc}, total {numJogador + numPc} é PAR!\n'
                  f'Você ganhou, parabéns! Vamos jogar novamente...')
        else:
            print(f'Você jogou {numJogador} e seu adversário jogou {numPc}, total {numJogador + numPc} é ÍMPAR!')
            break
    elif escolha.upper() == 'I':
        if res == 1:
            jogosGanhos += 1
            print(f'Você jogou {numJogador} e seu adversário jogou {numPc}, total {numJogador + numPc} é ÍMPAR!\n'
                  f'Você ganhou, parabéns! Vamos jogar novamente...')
        else:
            print(f'Você jogou {numJogador} e seu adversário jogou {numPc}, total {numJogador + numPc} é PAR!')
            break

print(f'Você teve {jogosGanhos} vitórias consecutivas e PERDEU, boa tentativa! Adeus...')
print('-=-' * 15)
