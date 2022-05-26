diaalug = int(input('\033[97mQuantos dias foi alugado? '))
kmrod = float(input('Quantos km rodados? '))
tot = (diaalug * 60) + (kmrod * 0.15)
print('\033[34mO total a pagar é de \033[32mR${0:.2f}.'.format(tot))