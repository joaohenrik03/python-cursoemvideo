# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

real = float(input('\033[97mQuanto de dinheiro você tem na carteira? R$: '))
cotacaodolar = 5.53
dolar = real / cotacaodolar
print('Com \033[32mR${:.2f} \033[97mvocê consegue comprar \033[32m${:.2f} \033[97mdólares!'.format(real, dolar))
