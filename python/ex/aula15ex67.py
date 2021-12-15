"""Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez,
 para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo."""
while True:
    num = int(input("Programa Tabuada!\nDigite um número: "))
    if num < 0:
        break
    print(f"Tabuada de {num}.")
    print(14 * "=")
    for i in range(1, 11):
        print(f" {num} x {i:2} = {num * i:2}")
    print(14 * "=")
print("Fim do programa!")