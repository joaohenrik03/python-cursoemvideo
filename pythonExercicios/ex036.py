# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valCasa = float(input('\033[34mValor da casa que deseja comprar: \033[32mR$'))
salario = float(input('\033[34mSalário do comprador: \033[32mR$'))
anos = int(input('\033[34mEm quantos anos você vai querer pagar? '))

prestacao = valCasa / (anos * 12)
cincoPctSalario = salario / 100 * 5
trintaPctSalario = cincoPctSalario * 6

print('\033[33m-=-=-=' * 10)
print('\033[97mVocê tem que pagar \033[32m{:.2f}\033[97m e o minimo é \033[32m{:.2f}.'
      .format(prestacao, trintaPctSalario))
if prestacao <= trintaPctSalario:
    print('\033[32mVocê pode financiar essa casa!')
    print('\033[32mVocê terá que pagar R${:.2f} por mês, durante {} anos.'.format(prestacao, anos))
else:
    print('\033[31mVocê não pode financiar essa casa!')
    print('\033[31mVocê terá que pagar R${:.2f} por mês, durante {} anos.'.format(prestacao, anos))
print('\033[33m-=-=-=' * 10)
