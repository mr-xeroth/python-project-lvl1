#!/usr/b:win/env python3
from ..cli import welcome_user
from ..core import brain_games_exec, unique_rand_list
from random import seed, randint

GAME_STEPS_COUNT = 3


def task_init():
    divisor_list = []

    seed(None)
    divisor_list = unique_rand_list(GAME_STEPS_COUNT, 3, 25)
    return divisor_list


# checks for correct numbers values
def is_valid(num_0, num_1):
    if num_0 == num_1 or (num_0 + num_1) % 2 == 0:
        return False
    # check with 50 and 100, etc
    if num_0 < num_1:
        if num_1 % num_0 == 0:
            return False
    else:
        if num_0 % num_1 == 0:
            return False
    return True


def task_gdc(op_list, step):
    divisor = op_list[step]
    num_limit = 100 // divisor
    num_0 = num_1 = 0
    while not is_valid(num_0, num_1):
        num_0 = randint(1, num_limit)
        num_1 = randint(1, num_limit)
    question_line = f"{num_0 * divisor} {num_1 * divisor}"
    solution_line = str(divisor)
    return [question_line, solution_line]


def input_validate(input_str):
    if input_str.lstrip('-').isdigit():
        return True
    else:
        return False


def answer_validate(input_str, solution_str):
    if input_str == solution_str:
        return True
    else:
        return False


def main():
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    prompt_line = 'Find the greatest common divisor of given numbers.'
    brain_games_exec(user_name, prompt_line, task_init, task_gdc,
                     GAME_STEPS_COUNT, input_validate, answer_validate)


if __name__ == '__main__':
    main()
