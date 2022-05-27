# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é o seu salário? R$: '))
umPct = salario / 100
cincoPct = umPct * 5

if salario <= 1250.0:
    quinzePct = cincoPct * 3
    novoSalario = salario + quinzePct
    print('Você terá um aumento de R${:.2f}(15%) no seu salário! Novo salário: R${:.2f}.'.format(quinzePct, novoSalario))
else:
    dezPct = cincoPct * 2
    novoSalario = salario + dezPct
    print('Você terá um aumento de R${:.2f}(10%) no seu salário! Novo salário: R${:.2f}.'.format(dezPct, novoSalario))
