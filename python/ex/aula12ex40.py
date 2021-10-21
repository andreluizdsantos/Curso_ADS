# 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print(f'APROVADO! Sua média é {media:.1f}')
elif 7 > media >= 5: # elif media >= 5 and media <= 7:
    print(f'EM RECUPERAÇÂO! Sua média é {media:.1f}')
else:
    print(f'REPROVADO! Sua média é {media:.1f}')
