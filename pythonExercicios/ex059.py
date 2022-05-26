from time import sleep
opcao = 0
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

while opcao != 5:
    print("""
    [1]Somar 
    [2]Multiplicar
    [3]Maior
    [4]Novos números
    [5]Sair do programa
    """)
    opcao = int(input('Opção: '))
    print('-=-=-=' * 8)

    if opcao == 1:
        soma = num1 + num2
        print('A soma entre {:.1f} e {:.1f} é igual a {:.1f}!'.format(num1, num2, soma))
        print('-=-=-=' * 8)
    elif opcao == 2:
        soma = num1 * num2
        print('A multiplicação de {:.1f} por {:.1f} é igual a {:.1f}!'.format(num1, num2, soma))
        print('-=-=-=' * 8)
    elif opcao == 3:
        maior = 0
        if num1 > num2:
            maior = num1
        elif num2 > num1:
            maior = num2
        print('O maior número digitado foi {:.1f}!'.format(maior))
        print('-=-=-=' * 8)
    elif opcao == 4:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
    elif opcao > 5:
        print('Ops, opção inválido, tente novamente!')
print('Saindo...')
sleep(2)

