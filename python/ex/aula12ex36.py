# 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
valor = float(input('Digite o valor do emprestimo: '))
salario = float(input('Digite o valor do seu salario: '))
parc = int(input('Digite a quantidade de parcelas para pagar: '))
if valor / parc > (salario * 0.3):
    print('Emprestimo não pode ser autorizado!')
else:
    print(f'Emprestimo autorizado, valor da parcela será: R${valor / parc:.2f}')
