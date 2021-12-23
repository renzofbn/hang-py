from Data.ascii_status import *


def clear():
    import os
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
                raise ValueError(
                    "\033[91mNo se permiten espacios en blaco, intenta de nuevo....")
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
                raise ValueError(
                    "No se aceptan respuestas en blanco, acaso quieres perder?")
            if c in chars:
                raise ValueError(
                    "Ya has ingresado esta letra anteriormente, ten cuidado!!")
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


def u_lose(name, chars, guess):
    print("¡No pudiste adivinar la palabra!", "\n")
    print(f"\033[95mLa palabra era: {guess}\033[0m", "\n")
    print("Las letras que ingresaste fueron -> ", end="")
    for letra in chars:
        print(letra, end=" ")
    print()
    print(f"{name}, gracia por jugar, hasta otra oportunidad", "\n" * 2)
    input("\033[93mPresiona enter para continuar \033[0m")
    print('\033[91m')


def new_game():
    import random
    with open('./Data/words.txt', 'r', encoding="utf-8") as file:
        words = [palabra[:-1] for palabra in file]

    guess = random.choice(words)
    right_a = [c for c in guess]
    dicc = map_word(guess)
    lines = [" _ " for _ in range(len(guess))]
    chars, r_chars, w_chars, errores, state = [], [], [], 0, 1
    return guess, right_a, dicc, lines, chars, r_chars, w_chars, errores, state


def bye():
    print("\nQue tengas buen día, gracias por jugar\n")
    input("\033[93mPresiona enter para continuar ")
    print('\033[92m')


def main_game(name):
    guess, right_a, dicc, lines, chars, r_chars, w_chars, errores, state = new_game()
    print('\033[93m', end="")
    while True:
        if errores < 10 and state == 1:
            hang_py(errores, state)
            print("¡Adivina la palabra¡")
            print()
            for line in lines:
                print(line, end="")
            print('\n')

            show_chars(chars, r_chars, w_chars)
            c = right_c(chars)
            chars.append(c)
            if dicc.get(c) is not None:
                r_chars.append(c)
                for a in dicc[c]:
                    lines[a] = c
                if lines == right_a:
                    clear()
                    state = 2
                print('\033[92m')
            else:
                print('\033[91m')
                w_chars.append(c)
                errores += 1
            clear()
        elif state == 2:
            clear()
            hang_py(errores, state)
            print("Bien jugado, adivinaste la palabra", guess)
            print("Las letras que ingresaste para hallarla fueron -> ", end="")
            for letra in chars:
                print(letra, end=" ")
            print()
            again = input(
                "\033[93m\n¿ Quieres seguir jugando ?  [s/n] \033[0m")
            if again == "s" or again == "S":
                guess, right_a, dicc, lines, chars, r_chars, w_chars, errores, state = new_game()
            else:
                state = 3
            clear()
        else:
            break

    if errores == 10:
        hang_py(errores, state)
        u_lose(name, chars, guess)
    else:
        tittle()
        bye()
    clear()
    game_over()
