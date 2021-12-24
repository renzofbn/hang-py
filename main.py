from src.ascii_status import tittle
from src.utilities import get_name, player, clear, main_game, show_top


def run():
    clear()
    tittle()
    print("¡ Bienvenid@ ! \n")
    name = get_name(name="")
    show_top()
    player(name)
    clear()
    main_game(name)


if __name__ == '__main__':
    run()
