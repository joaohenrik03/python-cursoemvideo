salario = float(input('Qual é o seu salário? R$'))
ump = salario / 100
cincop = ump * 5
if salario <= 1250.0:
    quinzep = cincop * 3
    novosal = salario + quinzep
    print('Você terá um aumento de R${:.2f}(15%) no seu salário! Novo salário: R${:.2f}.'.format(quinzep, novosal))
else:
    dezp = cincop * 2
    novosal = salario + dezp
    print('Você terá um aumento de R${:.2f}(10%) no seu salário! Novo salário: R${:.2f}.'.format(dezp, novosal))

