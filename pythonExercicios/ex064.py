num = 0
totNumeros = 0
somaNumeros = 0

while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        totNumeros += 1
        somaNumeros += num

print('Você digitou {} números e a soma entre eles foi {}.'.format(totNumeros, somaNumeros))

