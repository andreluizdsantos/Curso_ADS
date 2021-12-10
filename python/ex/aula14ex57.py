"""Exercício Python 57: Faça um programa que leia o sexo de uma pessoa,
 mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a
  digitação novamente até ter um valor correto."""
s = " "
while s not in 'MF':
    s = str(input("Digite o sexo [M/F]: ")).upper().strip()[0]
    if s not in 'MF':
        print("Opção inválida!")
print(f"Sexo digitado: {s}")
