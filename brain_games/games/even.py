#!/usr/bin/env python3

from brain_games.core import make_randint_array

game_list = []


# creates list of 3 ints
def init_game(step_count):
    global game_list
    game_list = make_randint_array(step_count, 1, 30)


# returns list ['question', 'solution']
def exec_game_step(step):
    solution_line = 'no' if game_list[step] % 2 else 'yes'
    question_line = str(game_list[step])
    return [question_line, solution_line]
