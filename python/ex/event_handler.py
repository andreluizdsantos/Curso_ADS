#Questão 2: Define os procedimentos de event handler
from pip._vendor.distlib.compat import raw_input


def handle_A():
    print("Wrong! Try again!")
def handle_B():
    print("Absolutely right! Trillium is a kind of flower!")
def handle_C():
    print("Wrong! Try again!")
#Questão 1: Define a aparência da tela
print("\n"*100) # clear the screen
print(" VERY CHALLENGING GUESSING GAME")
print("========================================================")
print("Press the letter of your answer, then the ENTER key.")
print("\n A. Animal")
print(" B. Vegetable")
print(" C. Mineral")
print(" X. Exit from this program\n")
print("========================================================")
print("What kind of thing is 'Trillium'?")
#Questão 4: O Event Loop. Loop eterno, esperando que algo aconteça.
while 1:
# Observamos o próximo evento
    answer = raw_input().upper()
# --------------------------------------------------------------
# Questão 3: Associamos os eventos de teclado que nos interessam
# com seus event handlers. Uma forma simples de binding.
# --------------------------------------------------------------
    if answer == "A": handle_A()
    if answer == "B": handle_B()
    if answer == "C": handle_C()
    if answer == "X":
# clear the screen and exit the event loop
        print("\n"*100)
        break
#Perceba que quaisquer outros eventos não interessam, por isso são ignorados.
