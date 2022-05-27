# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = primeiroTermo
maisTermo = 10
totTermos= 0

while maisTermo > 0:
    count = 1
    while count <= maisTermo:
        totTermos += 1

        print('{}'.format(termo), end=" -> ")
        termo += razao
        count += 1

    maisTermo = int(input('Quantos termos a mais você quer ver? '))

print(totTermos)
print('Acabou!')
