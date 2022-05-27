# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite um nome completo: ')).strip()
nomeDividido = nome.split()

print('Primeiro nome: {}'.format(nomeDividido[0]))
print('Último nome: {}'.format(nomeDividido[len(nomeDividido) - 1]))


