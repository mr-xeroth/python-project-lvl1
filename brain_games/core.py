#!/usr/bin/env python3
import prompt
from random import randint


def unique_rand_list(count, min, max):
    rnd_list = []
    num = 0
    while len(rnd_list) < count:
        while not num or num in rnd_list:
            num = randint(min, max)
        rnd_list.append(num)
    return rnd_list


def notify_and_quit(user, input_str, solution_str):
    str_reply = "'{}' is wrong answer ;(. Correct answer was '{}'."
    print(str_reply.format(input_str, solution_str))
    print(f"Let's try again, {user}!")
    quit()


def brain_games_exec(user, prompt_line, task_init, task_iterate, step_count,
                     is_input_valid, is_answer_valid):
    task_list = task_init()
    print(prompt_line)
    while step_count:
        task = task_iterate(task_list, step_count - 1)
        print(f'Question: {task[0]}')
        input_line = ""
        while not is_input_valid(input_line):
            input_line = prompt.string('Your answer: ')
        bool_correct = is_answer_valid(input_line, task[1])
        if bool_correct:
            print('Correct!')
            step_count -= 1
        else:
            notify_and_quit(user, input_line, task[1])
    print(f'Congratulations, {user}!')
