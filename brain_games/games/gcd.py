#!/usr/bin/env python3

from brain_games.core import make_randint_array
from random import randint

divisors = []


def init_game(step_count):
    global divisors
    divisors = make_randint_array(step_count, 3, 25)


# checks for correct numbers values
def is_num_valid(num_0, num_1):
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


def exec_game_step(step):
    divisor = divisors[step]
    num_limit = 100 // divisor
    num_0 = num_1 = 0
    while not is_num_valid(num_0, num_1):
        num_0 = randint(1, num_limit)
        num_1 = randint(1, num_limit)
    question_line = f"{num_0 * divisor} {num_1 * divisor}"
    solution_line = str(divisor)
    return [question_line, solution_line]
