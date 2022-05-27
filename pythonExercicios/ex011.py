# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m*2.

largura = float(input('\033[34mLargura da sua parede em metros: '))
altura = float(input('Altura da sua parede em metros: '))

m2 = altura * largura
tinta = m2 / 2

print('\033[33mSua parede tem \033[35m{:.2f}m²\033[33m, e para pintá-la você terá que usar \033[35m{:.2f}L '
      '\033[33mde tinta!'.format(m2, tinta))


