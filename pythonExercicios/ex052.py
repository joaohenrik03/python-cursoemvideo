# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[34m', end=" ")
        tot += 1
    else:
        print('\033[31m', end=" ")
    print('{}'.format(c), end=" ")
if tot == 2:
    print('\n\033[33mO {} é um número primo!'.format(num))
else:
    print('\n\033[33mO {} não é um número primo!'.format(num))
