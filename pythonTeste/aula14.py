'''for c in range(1, 5):
    num = int(input('Digite um valor: '))
print('Fim')'''

'''res = 'S'
while res == 'S':
    res = str(input('Quer continuar? S/N: ')).upper()
    print(res)
print('Fim')'''

num = 1
par = 0
impar = 0
while num != 0:
    num = int(input('Digite um valor:'))
    if num != 0:
        if num % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('Foi digitado {} números pares, e {} números ímpares!'.format(par, impar))
print('Acabou')
