#!/usr/bin/env python3
from brain_games.cli import welcome_user
import prompt
from random import seed

reply_line = "'{}' is wrong answer ;(. Correct answer was '{}'."


def run_game_package(exec_game_step, step_count):
    seed()

    print('Welcome to the Brain Games!')
    user_name = welcome_user()

    print(exec_game_step.game_prompt)
    while step_count:
        # returns list of strings [expression, solution]
        game_text = exec_game_step()
        print(f'Question: {game_text[0]}')

        input_line = prompt.string('Your answer: ')
        if input_line.casefold() == game_text[1]:
            print('Correct!')
            step_count -= 1
        else:
            print(reply_line.format(input_line, game_text[1]))
            print(f"Let's try again, {user_name}!")
            quit()
    print(f'Congratulations, {user_name}!')
