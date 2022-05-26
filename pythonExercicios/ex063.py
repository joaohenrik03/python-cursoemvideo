print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('SEQUÊNCIA FABONACCI')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')

termos = int(input('Quantos termos você quer ver? '))
c = 2
num = 0
num2 = 1

print("{} -> {}".format(num, num2), end=" -> ")
while c < termos:
    soma = num + num2
    print(soma, end=" -> ")
    num = num2
    num2 = soma

    c += 1

print('Acabou...')
