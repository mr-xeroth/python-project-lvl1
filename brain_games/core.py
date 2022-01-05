#!/usr/bin/env python3
import prompt


def notifyAndQuit(user, inputStr, solutStr):
    strReply = "'{}' is wrong answer ;(. Correct answer was '{}'."
    print(strReply.format(inputStr, solutStr))
    print(f"Let's try again, {user}!")
    quit()


def brainGamesExec(user, promptLine, taskInit, taskIterate, isInputValid,
                   isAnswerValid):
    taskList = taskInit()
    answerCount = 3
    print(promptLine)
    while answerCount:
        task = taskIterate(taskList, answerCount - 1)
        print(f'Question: {task[0]}')
        inputLine = ""
        while not isInputValid(inputLine):
            inputLine = prompt.string('Your answer: ')
        boolCorrect = isAnswerValid(inputLine, task[1])
        if boolCorrect:
            print('Correct!')
            answerCount -= 1
        else:
            notifyAndQuit(user, inputLine, task[1])
    print(f'Congratulations, {user}!')
