"""Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer
 mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos."""
print("Gerador de PA")
p = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
t2 = t = 10
c = 0
while t != 0:
    while c < t2:
        print(p, end=' ')
        p += r
        c += 1
    t = int(input("\nMais quantos termos quer exibir: "))
    t2 += t
print(f"Progressão finalizada com {c} temos exibidos!")
