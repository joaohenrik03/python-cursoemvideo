mreal = float(input('\033[97mQuanto de dinheiro você tem na carteira? '))
cotacaodolar = 5.53
mdolar = mreal / cotacaodolar
print('Com \033[32mR${:.2f} \033[97mvocê consegue comprar \033[32m${:.2f} \033[97mdólares!'.format(mreal, mdolar))
