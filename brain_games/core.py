#!/usr/bin/env python3
from brain_games.cli import welcome_user
import prompt
from random import seed

GAME_STEPS_COUNT = 3

reply_line = "'{}' is wrong answer ;(. Correct answer was '{}'."


def run_game_package(game_pack):
    seed()

    print('Welcome to the Brain Games!')
    user_name = welcome_user()

    print(game_pack.GAME_RULE)

    step_count = GAME_STEPS_COUNT

    while step_count:
        # get a couple of strings (question, solution)
        question, correct_answer = game_pack.get_game_strings()
        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')
        if user_answer.casefold() == correct_answer:
            print('Correct!')
            step_count -= 1
        else:
            print(reply_line.format(user_answer, correct_answer))
            print(f"Let's try again, {user_name}!")
            quit()
    print(f'Congratulations, {user_name}!')
