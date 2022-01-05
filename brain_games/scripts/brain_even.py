#!/usr/bin/env python3
from ..cli import welcome_user
from ..core import brainGamesExec
from random import seed, randint


def taskInit():
    randNum = []

    seed(None)
    num = 0
    while len(randNum) < 3:
        while not num or num in randNum:
            num = randint(1, 30)
        randNum.append(num)
    return randNum


# takes random number list [x, y, z]
# returns list ['question', 'solution']
def taskEven(numList, step):
    if numList[step] % 2:
        solutionLine = 'no'
    else:
        solutionLine = 'yes'
    questionLine = str(numList[step])
    return([questionLine, solutionLine])


def inputValidate(inputStr):
    str = inputStr.casefold()
    if str == 'yes' or str == 'no':
        return True
    return False


def answerValidate(inputStr, solutStr):
    if inputStr.casefold() == solutStr:
        return True
    return False


def main():
    print('Welcome to the Brain Games!')
    userName = welcome_user()
    promptLine = 'Answer "yes" if the number is even, otherwise answer "no".'
    brainGamesExec(userName, promptLine, taskInit, taskEven, inputValidate,
                   answerValidate)


if __name__ == '__main__':
    main()
