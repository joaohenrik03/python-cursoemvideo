from math import hypot
co = float(input('\033[35mComprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('\033[34mA hipotenusa irá medir \033[97m{:.2f}'.format(hi))


