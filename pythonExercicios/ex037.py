# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('\033[34mDigite um número inteiro: '))
print('\033[97m------' * 5)

base = int(input('''\033[34mEscolha qual será a base de conversão.
\033[35m[1]\033[34m para binário
\033[35m[2]\033[34m para octal
\033[35m[3]\033[34m para hexadecimal
\033[35mOPÇÃO: '''))

print('\033[97m-=-=-=' * 5)
if base == 1:
    binario = format(num, 'b')
    print('\033[32mResultado da conversão para binário: {}(dec) = {}(bin).'.format(num, binario))
elif base == 2:
    octal = format(num, 'o')
    print('\033[32mResultado da conversão para octal: {}(dec) = {}(octal).'.format(num, octal))
elif base == 3:
    hexa = format(num, 'x')
    print('\033[327mResultado da conversão para hexadecimal: {}(dec) = {}(hex).'.format(num, hexa))
else:
    print('\033[31m[ERRO] insira uma opção válida.')
print('\033[97m-=-=-=' * 5)

