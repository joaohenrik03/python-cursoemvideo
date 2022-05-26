num = int(input("Fatorial de: "))
contador = 1
res = 1

while contador <= 5:
    res = res * contador
    contador = contador + 1

print('O fatorial de {} é {}!'.format(num, res))
