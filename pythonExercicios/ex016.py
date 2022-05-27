# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

num = float(input('\033[97mDigite um valor: '))
print('\033[35mA parte inteira do número é: \033[4;34m{}'.format(int(num)))
