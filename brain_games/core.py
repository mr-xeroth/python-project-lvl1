#!/usr/bin/env python3
import brain_games.config
from brain_games.cli import welcome_user
import prompt
from random import seed, randint


# generate list of unique random ints, list[n] >= 0
def make_randint_array(count, base_value, top_value):
    if base_value < 0 or top_value < 0:
        print("make_randint_array(): limits' value must be >= 0")
        quit()

    random_list = []
    num = -1

    while len(random_list) < count:
        while num < 0 or num in random_list:
            num = randint(base_value, top_value)
        random_list.append(num)
    return random_list


def is_answer_valid_text(input_str, solution_str):
    if input_str.casefold() == solution_str:
        return True
    return False


def notify_and_quit(user_name, input_line, solution_line):
    reply_line = "'{}' is wrong answer ;(. Correct answer was '{}'."
    print(reply_line.format(input_line, solution_line))
    print(f"Let's try again, {user_name}!")
    quit()


def run_game_package():
    init_game = brain_games.config.init_game
    exec_game_step = brain_games.config.exec_game_step

    seed(None)

    print('Welcome to the Brain Games!')
    user_name = welcome_user()

    step_count = brain_games.config.game_steps_count
    # makes unique data for every game step
    init_game(step_count)

    print(brain_games.config.game_prompt)
    while step_count:
        # returns list of strings [expression, solution]
        game_step = exec_game_step(step_count - 1)
        print(f'Question: {game_step[0]}')
        input_line = prompt.string('Your answer: ')
        is_answer_correct = is_answer_valid_text(input_line, game_step[1])
        if is_answer_correct:
            print('Correct!')
            step_count -= 1
        else:
            notify_and_quit(user_name, input_line, game_step[1])
    print(f'Congratulations, {user_name}!')
