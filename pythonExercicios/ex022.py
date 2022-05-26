nome = str(input('Digite um nome: '))
nomedividido = nome.split()
print('Em maiúsculo: {}'.format(nome.upper()))
print('Em minúsculo: {}'.format(nome.lower()))
print('Quantidade total de letras: {}'.format(len(nome.strip()) - nome.count(' ')))
print('Quantidade de letras do primeiro nome: {}'.format(len(nomedividido[0])))

