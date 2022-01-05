#!/usr/bin/env python3
from ..cli import welcome_user
from ..core import brain_games_exec, unique_rand_list
from random import seed

GAME_STEPS_COUNT = 3


def task_init():
    rand_num = []

    seed(None)
    rand_num = unique_rand_list(GAME_STEPS_COUNT, 1, 30)
    return rand_num


# takes random number list [x, y, z]
# returns list ['question', 'solution']
def task_even(num_list, step):
    if num_list[step] % 2:
        solution_line = 'no'
    else:
        solution_line = 'yes'
    question_line = str(num_list[step])
    return [question_line, solution_line]


def input_validate(input_str):
    str = input_str.casefold()
    if str == 'yes' or str == 'no':
        return True
    return False


def answer_validate(input_str, solution_str):
    if input_str.casefold() == solution_str:
        return True
    return False


def main():
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    prompt_line = 'Answer "yes" if the number is even, otherwise answer "no".'
    brain_games_exec(user_name, prompt_line, task_init, task_even,
                     GAME_STEPS_COUNT, input_validate, answer_validate)


if __name__ == '__main__':
    main()
