# 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o valor do seu salário: '))
if salario > 1250:
    salario = salario * 1.1
    aumento = 10
else:
    salario = salario * 1.15
    aumento = 15
print(f'Você receberá um aumento de {aumento}% e seu salário será: R${salario:.2f}')
