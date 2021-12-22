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
    input('\033[93m¿List@ para jugar?  (Presiona enter para continuar)  \033[0m')


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


def get_name():
    while True:
        try:
            name = input("\033[94mPorfavor ingresa tu nombre: \033[0m")
            if len(name) == 0:
                raise ValueError("\033[91mNo se permiten espacios en blaco, intenta de nuevo....")
            break
        except ValueError as ve:
            print(ve)
            input("\033[93mPresiona enter para continuar ")
            print('\033[0m')
    return name


def right_c(chars):
    while True:
        try:
            c = input('\033[94mIngresa una letra: \033[0m').upper()
            if c.isdigit():
                raise ValueError("Solo se acpetan letras, ten cuidado!!")
            if len(c) > 1:
                raise ValueError("Ingresa una letra por vez, ten cuidado!!")
            if len(c) == 0:
                raise ValueError("No se aceptan respuestas en blanco, acaso quieres perder?")
            if c in chars:
                raise ValueError("Ya has ingresado esta letra anteriormente, ten cuidado!!")
            if not c.isalpha():
                raise ValueError("No se permiten caracteres, ten cuidado!!")
            break
        except ValueError as ve:
            print(f'\033[91m{ve}')
            input('\033[93m' + "Presiona enter para continuar " + '\033[0m')
            print()
    return c


def show_chars(chars, r_chars, w_chars):
    print("Letras ingresadas hasta ahora -> ", end="")
    for letra in chars:
        print(letra, end=" ")
    print()
    print("Letras correctas ingresadas hasta ahora -> ", end="")
    for letra in r_chars:
        print(letra, end=" ")
    print()
    print("Letras incorrectas ingresadas hasta ahora -> ", end="")
    for letra in w_chars:
        print(letra, end=" ")
    print('\n')

