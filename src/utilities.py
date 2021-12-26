from src.ascii_status import *


def clear():
    import os
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def player(name):
    print()
    print(f"{name}, espero que te diviertas jugando a Hang-py  :D")
    print("Las reglas son simples, tienes 10 intentos para adivinar la totalidad")
    print("de letras que conforman una palabra, escogida al azar.")
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


def get_name(name):
    while True:
        try:
            name = name + \
                input(f"\033[94mPor favor ingresa tu nombre: \033[0m {name}")
            if len(name) == 0:
                raise ValueError(
                    "\033[91mNo se permiten espacios en blanco, intenta de nuevo....")
            if len(name) > 15:
                raise ValueError(
                    "\033[91mTu nombre es muy largo, intenta de nuevo....")
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
                raise ValueError("Solo se aceptan letras, ten cuidado!!")
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
    print("\033[93mLetras ingresadas hasta ahora -> \033[0m", end="")
    for letra in chars:
        print(letra, end=" ")
    print()
    print("\033[92mLetras correctas ingresadas hasta ahora -> \033[0m", end="")
    for letra in r_chars:
        print(letra, end=" ")
    print()
    print("\033[91mLetras incorrectas ingresadas hasta ahora -> \033[0m", end="")
    for letra in w_chars:
        print(letra, end=" ")
    print('\n')


def u_lose(chars, guess, points):
    print("¡No pudiste adivinar la palabra!", "\n")
    print(f"\033[95mLa palabra era: {guess}\033[0m", "\n")
    print("Las letras que ingresaste fueron -> ", end="")
    for letra in chars:
        print(letra, end=" ")
    print()
    if points < 0:
        print("No has conseguido ningún punto")
    else:
        print(f"Has conseguido {points} puntos.")
    input("\033[93mPresiona enter para continuar \033[0m")
    print('\033[91m')


def new_game(words):
    import random
    guess = random.choice(words)
    words.remove(guess)
    right_a = [c for c in guess]
    dicc = map_word(guess)
    lines = [" _ " for _ in range(len(guess))]
    chars, r_chars, w_chars, errores, state = [], [], [], 0, 1
    return guess, right_a, dicc, lines, chars, r_chars, w_chars, errores, state, words


def bye(position, data, points, name):
    if position != 0:
        print("\n")
        print(f"\033[92mHas llegado al puesto N° {position} !!!")
        n_top = get_name(name)
        if position == 1:
            data[1] = str(points) + "\n"
            data[0] = n_top + "\n"
        if position == 2:
            data[3] = str(points) + "\n"
            data[2] = n_top + "\n"
        if position == 3:
            data[5] = str(points) + "\n"
            data[4] = n_top + "\n"
        save_top(data)
    else:
        print("No has obtenido los suficientes puntos para llegar al top :(")
    print("\nQue tengas buen día, gracias por jugar\n")
    input("\033[93mPresiona enter para continuar ")
    print('\033[92m')


def save_top(data):
    a = ["## TOP SCORES ##\n", "\n", data[0], data[1], data[2], data[3], data[4], data[5], "\n",
         "# DO NOT MODIFY THIS FILE // NO MODIFICAR"]
    with open("./src/top.txt", 'w', encoding='utf-8') as f:
        for name in a:
            f.write(name)


def top(points, data):
    print('\033[92m', end="")
    if points >= int(data[1]):
        print("Estás rompiendo un récord, estás primero!!!!")
        position = 1
    elif points >= int(data[3]):
        print("Felicidades, te encuentras en el segundo puesto!!")
        print(
            f"Tan solo {int(data[1]) - points} punto(s) para romper un récord!!")
        position = 2
    elif points >= int(data[5]):
        print("Nada mal, estas en tercer puesto")
        print(f"Necesitas {int(data[3]) - points} punto(s) para ser segundo!!")
        position = 3
    else:
        print(
            f"Sigue así, te falta {int(data[5]) - points} puntos para estar 3°")
        position = 0
    print('\033[0m', end="")
    return position


def show_top():
    with open("./src/top.txt", 'r', encoding="utf-8") as f:
        data = f.readlines()[2:8]
        data = [palabra[:-1] for palabra in data]
    print(
        f"\033[95m\nTOP PLAYERS\n-----------------------\033[0m\n\n1){data[0]} -> {data[1]}")
    print(f"2){data[2]} -> {data[3]}\n3){data[4]} -> {data[5]}")
    print("\n\033[95m-----------------------\033[0m")


def main_game(name):
    with open("./src/top.txt", 'r', encoding="utf-8") as f:
        data = f.readlines()[2:8]
    with open('./src/words.txt', 'r', encoding="utf-8") as file:
        words = [palabra[:-1] for palabra in file]
    position = 0
    points = 0
    guess, right_a, dicc, lines, chars, r_chars, w_chars, errores, state, words = new_game(
        words)
    print('\033[93m', end="")
    while True:
        if errores < 10 and state == 1:
            hang_py(errores, state)
            print(f"¡{name}, adivina la palabra¡")
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
                points -= 1
                errores += 1
            clear()
        elif state == 2:
            points += 20
            clear()
            hang_py(errores, state)
            print(f"{name}, adivinaste la palabra", guess)
            print("Letras ingresadas -> ", end="")
            for letra in chars:
                print(letra, end=" ")
            print(f"\nHas conseguido {points} puntos hasta ahora\n")
            position = top(points, data)
            again = input(
                f"\033[93m\n¿{name}, quieres seguir jugando? [s/n] \033[0m")
            if again == "s" or again == "S" or len(again) == 0:
                guess, right_a, dicc, lines, chars, r_chars, w_chars, errores, state, words = new_game(
                    words)
            else:
                state = 3
            clear()
        else:
            break

    if errores == 10:
        hang_py(errores, state)
        u_lose(chars, guess, points)
        position = top(points, data)
        clear()
        tittle()
        bye(position, data, points, name)
        if position == 0:
            print('\033[91m', end="")
    else:
        tittle()
        bye(position, data, points, name)
    clear()
    game_over()
    print(words)
