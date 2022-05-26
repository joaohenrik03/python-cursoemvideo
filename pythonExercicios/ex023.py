#num = str(input('Digite um número de 0 a 9999: '))
#print('Unidade: {}'.format(num[3:]))
#print('Dezena: {}'.format(num[2:3]))
#print('Centena: {}'.format(num[1:2]))
#print('Milhar: {}'.format(num[:1]))

num = int(input('Digite um número de 0 a 9999: '))
uni = num // 1 % 10
dez = num // 10 % 10
cent = num // 100 % 10
mili = num // 1000 % 10
print('Unidade: {}'.format(uni))
print('Dezena: {}'.format(dez))
print('Centena: {}'.format(cent))
print('Miliar: {}'.format(mili))


