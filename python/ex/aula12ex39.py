# 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do
# tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
if idade == 18:
    print(f'Você tem {idade} anos e precisa fazer o alistamento Militar imediatamente!')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o seu alistamento, que será em {nasc + 18}')
else:
    print(f'Seu alistamento já passou {idade - 18} anos e deveria ser feito em {nasc + 18}')
