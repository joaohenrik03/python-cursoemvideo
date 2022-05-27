# Faça um algoritmo que leia o salário de um funcionário(a) e mostre o seu novo salário com 15% de aumento.

salario = float(input('\033[97mQual o valor do seu salário? '))

cincoPct = (salario / 100) * 5
quinzePct = cincoPct * 3
salarioTot = salario + quinzePct

print('\033[93mEsté mês você irá receber \033[32m15% \033[93mde aumento, e seu salário total será: \033[32mR${:.2f}'
      .format(salarioTot))
