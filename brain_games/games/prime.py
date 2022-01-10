#!/usr/bin/env python3

from brain_games.core import make_randint_array

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
    def is_in_prime_list():
        global int_list
        print('ints:', int_list)
        for i in int_list:
            if i in prime_ints:
                return True
        return False

    while not is_in_prime_list():
        int_list = make_randint_array(step_count, 2, prime_limit)
    print(int_list)
    print('Done init')


# returns list ['question', 'solution']
def exec_game_step(step):
    question_line = 'NoS'
    solution_line = 'NoS'

    solution_line = 'yes' if int_list[step] in prime_ints else 'no'
    question_line = str(int_list[step])
    return [question_line, solution_line]
