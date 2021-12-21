from Data.ascii_status import *
from Data.utilities import *
import random


def run():
    tittle()
    print("¡ Bienvenid@ !")
    name = input("Porfavor ingresa tu nombre: ")
    player(name)
    clear()
    errores = 0
    with open("./Data/words.txt", 'r', encoding="utf-8") as file:
        words = [palabra[:-1] for palabra in file]
    guess = random.choice(words)
    right_a = [c for c in guess]
    dicc = map_word(guess)
    lines = ["_" for _ in range(len(guess))]
    chars = []
    while True:
        if errores < 10:
            print(dicc)
            hang_py(errores)
            print("¡Adivina la palabra¡")
            for line in lines:
                print(line, end="")
            print()

            print("Letra ingresadas hasta ahora -> ", end="")
            for letra in chars:
                print(letra, end=" ")
            print()

            c = input("Ingresa una letra: ").upper()
            chars.append(c)
            if dicc.get(c) is not None:
                for a in dicc[c]:
                    lines[a] = c
                if lines == right_a:
                    clear()
                    errores=20
            else:
                errores += 1
            clear()
        elif errores == 20:
            clear()
            hang_py(errores)
            print("Bien jugado, adivinaste la palabra", guess)
            print("Las letras que ingresaste para hallarla fueron -> ", end="")
            for letra in chars:
                print(letra, end=" ")
            print()
            again = input("¿ Quieres seguir jugando ?  [s/n] ")
            if again == "s" or again == "S":
                guess = random.choice(words)
                right_a = [c for c in guess]
                dicc = map_word(guess)
                lines = ["_" for _ in range(len(guess))]
                chars = []
                errores = 0
            else:
                errores=100
            clear()
        else:
            break

    if errores == 10:
        hang_py(errores)
        print("¡No pudiste adivinar la palabra!", "\n")
        print(f"La palabra era: {guess}", "\n")
        print("Las letras que ingresaste fueron -> ", end="")
        for letra in chars:
            print(letra, end=" ")
        print()
        print(f"{name}, gracia por jugar, hasta otra oportunidad", "\n" * 2)
        input("Presiona enter para continuar ")
        print('\033[91m')
    else:
        print("Que tengas buen día, gracias por jugar")
        input("Presiona enter para continuar ")
        print('\033[92m')
    clear()
    game_over()


if __name__ == '__main__':
    run()
