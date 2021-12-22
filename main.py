from Data.ascii_status import tittle
from Data.utilities import get_name, player, clear, main_game


def run():
    tittle()
    print("¡ Bienvenid@ ! \n")
    name = get_name()
    player(name)
    clear()
    main_game(name)


if __name__ == '__main__':
    run()
