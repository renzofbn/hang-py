import os


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def player(name):
    print()
    print(f"{name}, espero que te diviertas jugando a Hang-py  :D")
    print("Las reglas son simples, tienes 10 intentos para adivinar la totalidad de letras ")
    print("que conforman una palabra, escogida al azar")
    print()
    input("¿List@ para jugar?  (Presiona enter para continuar)  ")


def map_word(word):
    dicc = {}
    cont = 0
    for caracter in word:
        if caracter in dicc:
            dicc[caracter] += [cont]
        else:
            dicc[caracter] = [cont]
        cont += 1
    return dicc
