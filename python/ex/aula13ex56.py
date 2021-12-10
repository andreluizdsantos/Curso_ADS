"""Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
 No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais
  velho e quantas mulheres têm menos de 20 anos."""
somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
tot = 0
for p in range(1, 5):
    nome = input(f"{p}ª pessoa.\nNome: ")
    idade = int(input(f"Idade: "))
    sexo = input(f"Sexo [M/F]: ")
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    elif idade > maioridadehomem and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        tot += 1
médiaidade = somaidade / 4
print(f"A média de idade do grupo é de {médiaidade} anos.")
if nomevelho != '':
    print(f"O homem mais velho se chama {nomevelho} e tem {maioridadehomem} anos.")
print(f"Total de mulheres com menos de 20 anos: {tot}")
