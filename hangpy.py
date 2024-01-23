from src.ascii_status import tittle
from src.utilities import get_name, clear, main_game, show_top


def run():
    clear()
    tittle()
    name = get_name(name="")
    clear()
    main_game(name)


if __name__ == '__main__':
    run()
