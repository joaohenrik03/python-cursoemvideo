import random
import time

numPc = numJogador = 0
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
            print(f'Você jogou {numJogador} e seu adversário jogou {numPc}, total {numJogador + numPc} é PAR!\n'
                  f'Você ganhou, parabéns! Vamos jogar novamente...')
        else:
            print(f'Você jogou {numJogador} e seu adversário jogou {numPc}, total {numJogador + numPc} é ÍMPAR!\n'
                  f'Você perdeu, boa tentativa! Adeus...')
            break
    elif escolha.upper() == 'I':
        if res == 1:
            print(f'Você jogou {numJogador} e seu adversário jogou {numPc}, total {numJogador + numPc} é ÍMPAR!\n'
                  f'Você ganhou, parabéns! Vamos jogar novamente...')
        else:
            print(f'Você jogou {numJogador} e seu adversário jogou {numPc}, total {numJogador + numPc} é PAR!\n'
                  f'Você perdeu, boa tentativa! Adeus...')
            break

print('-=-' * 15)
