nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('=-=-=-=-=' * 4)
print('Sua média foi {:.1f}'.format(media))
if media < 5:
    print('Você foi REPROVADO!')
elif 7 > media >= 5:
    print('Você está de RECUPERAÇÃO, estude mais!')
else:
    print('Você foi APROVADO, continue assim!')
print('=-=-=-=-=' * 4)