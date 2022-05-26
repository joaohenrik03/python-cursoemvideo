primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
enesimoTermo = primeiroTermo + (10-1) * razao
count = primeiroTermo

while count < enesimoTermo+razao:
    print('{}'.format(count), end=" -> ")
    count += razao

print('Acabou!')
