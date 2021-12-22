from Data.ascii_status import *
from Data.utilities import *
import random


def run():
    tittle()
    print("¡ Bienvenid@ ! \n")
    name = get_name()
    player(name)
    clear()
    with open("./Data/words.txt", 'r', encoding="utf-8") as file:
        words = [palabra[:-1] for palabra in file]
    guess = random.choice(words)
    right_a = [c for c in guess]
    dicc = map_word(guess)
    lines = [" _ " for _ in range(len(guess))]
    chars, r_chars, w_chars, errores = [], [], [], 0
    state = 1   # 1 is for game, 2 is for correct answer, 3 is for leave game
    while True:
        if errores < 10 and state == 1:
            hang_py(errores)
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
                    state= 2
                print('\033[92m')
            else:
                print('\033[91m')
                w_chars.append(c)
                errores += 1
            clear()
        elif state == 2:
            clear()
            hang_py(errores)
            print("Bien jugado, adivinaste la palabra", guess)
            print("Las letras que ingresaste para hallarla fueron -> ", end="")
            for letra in chars:
                print(letra, end=" ")
            print()
            again = input("\033[93m\n¿ Quieres seguir jugando ?  [s/n] \033[0m")
            if again == "s" or again == "S":
                guess = random.choice(words)
                right_a = [c for c in guess]
                dicc = map_word(guess)
                lines = [" _ " for _ in range(len(guess))]
                chars, r_chars, w_chars, errores, state = [], [], [], 0, 1
            else:
                state = 3
            clear()
        else:
            break

    if errores == 10:
        hang_py(errores)
        print("¡No pudiste adivinar la palabra!", "\n")
        print(f"\033[95mLa palabra era: {guess}\033[0m", "\n")
        print("Las letras que ingresaste fueron -> ", end="")
        for letra in chars:
            print(letra, end=" ")
        print()
        print(f"{name}, gracia por jugar, hasta otra oportunidad", "\n" * 2)
        input("\033[93mPresiona enter para continuar \033[0m")
        print('\033[91m')
    else:
        print("Que tengas buen día, gracias por jugar\n")
        input("\033[93mPresiona enter para continuar ")
        print('\033[92m')
    clear()
    game_over()


if __name__ == '__main__':
    run()
