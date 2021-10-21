#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros
valor = int(input("Digite o valor: "))
parcelas = 0
total = 0
opcao = int(input("""Escolha uma forma de pagamento:
1-À vista Dinheiro/Cheque:
2-Cartão à vista:
3-Cartão até 2X:
4-Cartão em 3X ou mais:"""))
if opcao == 1:
    total = valor - (valor * 10 / 100)
    print("Valor total: {:.2f} pago à vista com 10% de desconto.".format(total))
elif opcao == 2:
    total = valor - (valor * 5 / 100)
    print("Valor total: {:.2f} pago à vista no cartão com 5% de desconto.".format(total))
elif opcao == 3:
    print("Valor total: {:.2f} sem juros.".format(valor))
elif opcao == 4:
    total = valor + (valor * 20 / 100)
    parcelas = int(input("Em quantas parcelas? "))
    print("Valor total: {:.2f} pago em {}X de {:.2f} com 20% de juros.".format(total, parcelas, (total / parcelas)))
else:
    print("Opção inválida.")
