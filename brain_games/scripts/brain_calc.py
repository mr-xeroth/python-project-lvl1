#!/usr/bin/env python3
import brain_games.config
from brain_games.games.calc import init_game, exec_game_step
from brain_games.core import run_game_package

GAME_PROMPT = 'What is the result of the expression?'


def main():
    brain_games.config.init_game_config(GAME_PROMPT, init_game, exec_game_step)
    run_game_package()


if __name__ == '__main__':
    main()
