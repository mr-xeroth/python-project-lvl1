#!/usr/b:win/env python3
from ..cli import welcome_user
from ..core import brain_games_exec, unique_rand_list
from random import seed

GAME_STEPS_COUNT = 3
prime_num_list = []


def prime_list_calc(max):
    global prime_num_list
    prime_num_list.append(2)
    for i in range(3, max):
        division_count = 0
        for j in range(2, i - 1):
            if not i % j:
                division_count += 1
        if not division_count:
            prime_num_list.append(i)


def task_init():
    global prime_num_list
    seed(None)
    prime_list_calc(100)

    # ought to contain at least 1 prime number
    def in_prime_list(op_list):
        for i in op_list:
            if i in prime_num_list:
                return True
        return False
    op_list = []
    while not in_prime_list(op_list):
        op_list = unique_rand_list(GAME_STEPS_COUNT, 2, 100)
    return op_list


# takes random numbers list [x, y, z]
# returns list ['question', 'solution']
def task_prime(op_list, step):
    global prime_num_list
    if op_list[step] in prime_num_list:
        solution_line = 'yes'
    else:
        solution_line = 'no'
    question_line = str(op_list[step])
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
    prompt_line = 'Answer "yes" if given number is prime.' \
                  ' Otherwise answer "no".'
    brain_games_exec(user_name, prompt_line, task_init, task_prime,
                     GAME_STEPS_COUNT, input_validate, answer_validate)


if __name__ == '__main__':
    main()
