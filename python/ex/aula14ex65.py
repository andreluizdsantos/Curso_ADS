"""Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
 No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
  O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""
num = cont = soma = media = menor = maior = 0
resp = 'S'
while resp in "S":
    num = int(input("Digite um número: "))
    cont += 1
    soma += num
    if menor > num or cont == 1:
        menor = num
    if maior < num:
        maior = num
    resp = str(input("Continuar [S/N]: ")).strip().upper()[0]
media = soma / cont
print(f"Média: {media}, do total de {cont}, valores lidos.")
print(f"Maior valor lido: {maior}")
print(f"Menor valor lido: {menor}")
