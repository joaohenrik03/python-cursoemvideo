# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

print('\033[97m======= \033[4;34mLOJAS THREE\033[0;97m =======')
preco = float(input('\033[35mPreço das compras: \033[32mR$'))
formas = int(input('''\033[1;34mFORMAS DE PAGAMENTO
\033[0;34m[ 1 ] \033[35mà vista dinheiro/cheque
\033[34m[ 2 ] \033[35mà vista cartão
\033[34m[ 3 ] \033[35m2x no cartão
\033[34m[ 4 ] \033[35m3x ou mais no cartão 
\033[1;34mQual é a sua opção? '''))
print('\033[97m=-=-=-=\033[m' * 6)

if formas == 1:
    descontoDez = (preco / 10)
    print('\033[32mSua compra de R${:.2f} vai custar R${:.2f} no final.\033[m'.format(preco, (preco - descontoDez)))
elif formas == 2:
    descontoCinco = (preco / 100) * 5
    print('\033[32mSua compra de R${:.2f} vai custar R${:.2f} no final.\033[m'.format(preco, (preco - descontoCinco)))
elif formas == 3:
    print('\033[32mSua compra de R${:.2f} vai continuar com o mesmo preço.\033[m'.format(preco))
elif formas == 4:
    parcelas = int(input('\033[34mQuantas parcelas? \033[m'))
    if parcelas < 3:
        print('\033[97m=-=-=-=\033[m' * 6)
        print('\033[31m[ERRO] Dado inválido, tente novamente.\033[m')
    else:
        jurosVinte = (preco / 10) * 2
        total = preco + jurosVinte
        print('\033[97m=-=-=-=\033[m' * 6)
        print('\033[32mSua compra será parcelada em {}x de R${} com 20% de JUROS.\033[m'
              .format(parcelas, (total / parcelas)))
        print('\033[32mSua compra de R${:.2f} vai custar R${} no final.\033[m'.format(preco, total))
else:
    print('\033[97m=-=-=-=\033[m' * 6)
    print('\033[31m[ERRO] Dado inválido, tente novamente.')

print('\033[97m=-=-=-=\033[m' * 6)
