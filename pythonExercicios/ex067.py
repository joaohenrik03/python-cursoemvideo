num = 0
while True:
    print('-=-=-=-=-=-=-=-=-=-=-')
    num = int(input('Digite um número: '))
    print('-=-=-=-=-=-=-=-=-=-=-')
    if num < 0:
        break
    for cont in range(1, 11):
        print(f'{cont} X {num} = {cont * num}')

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
