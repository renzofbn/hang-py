import os
from Data.ascii_status import *


def run():
    def clear():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    for i in range(11):
        clear()
        hang_py(i)
        input("")


if __name__ == '__main__':
    run()
