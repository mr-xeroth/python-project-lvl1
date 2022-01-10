#!/usr/bin/env python3
import brain_games.config
from brain_games.games.progression import init_game, exec_game_step
from brain_games.core import run_game_package

GAME_PROMPT = 'Answer "yes" if given number is prime.' \
              ' Otherwise answer "no".'
brain_games.config.game_prompt = GAME_PROMPT
brain_games.config.game_steps_count = 3
brain_games.config.init_game = init_game
brain_games.config.exec_game_step = exec_game_step


def main():
    run_game_package()


if __name__ == '__main__':
    main()
