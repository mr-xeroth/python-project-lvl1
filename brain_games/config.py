# global var definition for modules

game_prompt = 'no prompt'
game_steps_count = 1
init_game = None
exec_game_step = None


def init_game_config(prompt_line, init_proc, exec_proc, steps=3):
    global game_prompt
    global game_steps_count
    global init_game
    global exec_game_step

    game_prompt = prompt_line
    game_steps_count = steps
    init_game = init_proc
    exec_game_step = exec_proc
