"""Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos."""
maior = masc = femimenor = 0
while True:
    idade = int(input("Digite a idade: "))
    sexo = r = ' '
    while sexo not in 'MF':
        sexo = str(input("Digite o sexo: [M/F]")).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo in 'M':
        masc += 1
    if sexo in 'F' and idade < 20:
        femimenor += 1
    while r not in 'SN':
        r = str(input("Deseja realizar novo cadastro? [S/N]")).strip().upper()[0]
    if r in 'N':
        break
print(f"Total de pessoas maiores de 18 anos: {maior}")
print(f"Total de homens cadastrados: {masc}")
print(f"Total de mulheres com menos de 20 anos: {femimenor}")
