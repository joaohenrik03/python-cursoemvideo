'''from math import trunc
num = float(input('Digite um número: '))
print('A parte inteira do número é: {}'.format(trunc(num)))'''

num = float(input('\033[97mDigite um valor: '))
print('\033[35mA parte inteira do número é: \033[4;34m{}'.format(int(num)))