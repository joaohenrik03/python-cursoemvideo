primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiroTermo
count = 1

while count <= 10:
    print('{}'.format(termo), end=" -> ")
    termo += razao
    count += 1

print('Acabou!')
