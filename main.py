#!/usr/bin/python3

import greeting
import game_loop


if __name__ == '__main__':
    # Приветствие и правила игры
    game_loop.clear_console()
    greeting.greeting()
    while True:
        # Начинаем игру))
        game_loop.clear_console()
        game_loop.Game()
        if not game_loop.Game.play_again():
            break
