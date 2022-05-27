# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

valorProduto = float(input('\033[97mQual o valor do produto que deseja comprar? '))
descontoCinco = (valorProduto / 100) * 5
descontoTot = valorProduto - descontoCinco
print('\033[34mNa liquidação, esse produto que custa \033[32mR${:.2f} terá 5% \033[34mde desconto. '
      '\nEle vai ficar custando apenas \033[32mR${:.2f}!'.format(valorProduto, descontoTot))
