#!/usr/bin/env python3
from brain_games.games.prime import exec_game_step
from brain_games.core import run_game_package

GAME_STEPS_COUNT = 3


def main():
    run_game_package(exec_game_step, GAME_STEPS_COUNT)


if __name__ == '__main__':
    main()
