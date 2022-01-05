#!/usr/b:win/env python3
from ..cli import welcome_user
from ..core import brainGamesExec
from random import seed, randint


def taskInit():
    divisorList = []
    seed(None)
    num = 0
    while len(divisorList) < 3:
        while not num or num in divisorList:
            num = randint(3, 25)
        divisorList.append(num)
    return divisorList


def taskGDC(opList, step):
    def isValid(op0, op1):
        if op0 == op1:
            return False
        if (op0 + op1) % 2 == 0:
            return False
        return True
    divisor = opList[step]
    limit = 100 // divisor
    op0 = op1 = 0
    while not isValid(op0, op1):
        op0 = randint(1, limit)
        op1 = randint(1, limit)
    questionLine = f"{op0 * divisor} {op1 * divisor}"
    solutionLine = str(divisor)
    return [questionLine, solutionLine]


def inputValidate(inputStr):
    if inputStr.lstrip('-').isdigit():
        return True
    else:
        return False


def answerValidate(inputStr, solutStr):
    if inputStr == solutStr:
        return True
    else:
        return False


def main():
    print('Welcome to the Brain Games!')
    userName = welcome_user()
    promptLine = 'Find the greatest common divisor of given numbers.'
    brainGamesExec(userName, promptLine, taskInit, taskGDC, inputValidate,
                   answerValidate)


if __name__ == '__main__':
    main()
