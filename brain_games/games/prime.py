#!/usr/bin/env python3

from brain_games.core import make_randint_array
from random import randint

prime_ints = []
prime_limit = 100
int_list = []


def is_prime(num):
    if num < 2:
        return False

    divider = 2

    while divider <= num / 2:
        if num % divider == 0:
            return False
        divider += 1
    return True


def prime_list_calc(top_value):
    global prime_ints
    for i in range(2, top_value):
        if is_prime(i):
            prime_ints.append(i)


# makes random numbers list [x, y, z]
def init_game(step_count):
    global int_list
    prime_list_calc(prime_limit)

    # ought to contain at least 1 prime number
    int_list = make_randint_array(step_count, 2, prime_limit)
    index = randint(0, step_count - 1)
    prime_index = randint(0, len(prime_ints) - 1)
    int_list[index] = prime_ints[prime_index]


# returns list ['question', 'solution']
def exec_game_step(step):
    question_line = 'NoS'
    solution_line = 'NoS'

    solution_line = 'yes' if int_list[step] in prime_ints else 'no'
    question_line = str(int_list[step])
    return [question_line, solution_line]
