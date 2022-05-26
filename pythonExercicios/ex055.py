maior = 0
manor = 0
for cont in range(0, 5):
    peso = float(input('Qual é o seu peso? Kg'))
    if cont == 0:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O menor peso foi {}, o maior foi {}.'.format(menor, maior))
