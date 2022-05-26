valcasa = float(input('\033[34mValor da casa que deseja comprar: \033[32mR$'))
salario = float(input('\033[34mSalário do comprador: \033[32mR$'))
anos = int(input('\033[34mEm quantos anos você vai querer pagar? '))

prestacao = valcasa / (anos * 12)
cincopsal = salario / 100 * 5
trintapsal = cincopsal * 6

print('\033[33m-=-=-=' * 10)
print('\033[97mVocê tem que pagar \033[32m{:.2f}\033[97m e o minimo é \033[32m{:.2f}.'.format(prestacao, trintapsal))
if prestacao <= trintapsal:
    print('\033[32mVocê pode financiar essa casa!')
    print('\033[32mVocê terá que pagar R${:.2f} por mês, durante {} anos.'.format(prestacao, anos))
else:
    print('\033[31mVocê não pode financiar essa casa!')
    print('\033[31mVocê terá que pagar R${:.2f} por mês, durante {} anos.'.format(prestacao, anos))
print('\033[33m-=-=-=' * 10)
