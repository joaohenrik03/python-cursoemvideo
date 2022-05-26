largura = float(input('\033[34mQual a largura da sua parede em metros? '))
altura = float(input('Qual é a altura da sua parede em metros? '))
m2 = altura * largura
tinta = m2 / 2
print('\033[33mSua parede tem \033[35m{:.2f}m²\033[33m, e para pintar ela você irá ter que usar \033[35m{:.2f}L '
      '\033[33mde tinta!'.format(m2, tinta))


