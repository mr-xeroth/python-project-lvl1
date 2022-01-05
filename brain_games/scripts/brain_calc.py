#!/usr/b:win/env python3
from ..cli import welcome_user
from ..core import brainGamesExec
from random import seed, randint


mathOps = ['nop', 'sum', 'sub', 'mul']


def taskInit():
    mathOpList = []

    seed(None)
    mathOpNdx = 0
    while len(mathOpList) < 3:
        while not mathOpNdx or mathOpNdx in mathOpList:
            mathOpNdx = randint(1, 3)
        mathOpList.append(mathOpNdx)
    return mathOpList


# takes randomly ordered list [1, 2, 3] for op codes
# returns list ['question', 'solution']
def taskCalc(opList, step):
    if mathOps[opList[step]] == 'sum' or mathOps[opList[step]] == 'sub':
        oper0 = randint(3, 99)
        oper1 = randint(3, 99)
        if mathOps[opList[step]] == 'sum':
            questionLine = f'{oper0} + {oper1}'
            solutionLine = str(oper0 + oper1)
        else:
            questionLine = f'{oper0} - {oper1}'
            solutionLine = str(oper0 - oper1)
    elif mathOps[opList[step]] == 'mul':
        oper0 = randint(11, 99)
        oper1 = randint(3, 9)
        questionLine = f'{oper0} * {oper1}'
        solutionLine = str(oper0 * oper1)
    return([questionLine, solutionLine])


def inputValidate(inputStr):
    if inputStr != "" and inputStr.lstrip('-').isdigit():
        return True
    return False


def answerValidate(inputStr, solutStr):
    if inputStr == solutStr:
        return True
    return False


def main():
    print('Welcome to the Brain Games!')
    userName = welcome_user()
    promptLine = 'What is the result of the expression?'
    brainGamesExec(userName, promptLine, taskInit, taskCalc, inputValidate,
                   answerValidate)


if __name__ == '__main__':
    main()
