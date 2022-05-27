# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

diasAlugados = int(input('\033[97mQuantos dias foi alugado? '))
kmRodado = float(input('Quantos km rodados? '))
tot = (diasAlugados * 60) + (kmRodado * 0.15)
print('\033[34mO total a pagar é de \033[32mR${0:.2f}.'.format(tot))
