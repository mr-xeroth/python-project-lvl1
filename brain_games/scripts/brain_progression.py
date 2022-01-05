#!/usr/b:win/env python3
from ..cli import welcome_user
from ..core import brainGamesExec
from random import seed, randint


def taskInit():
    def uniqueRandList(count, min, max):
        rndList = []
        num = 0
        while len(rndList) < count:
            while not num or num in rndList:
                num = randint(min, max)
            rndList.append(num)
        return rndList

    seed(None)
    lenList = startList = stepList = skipList = []
    lenList = uniqueRandList(3, 6, 10)
    startList = uniqueRandList(3, 2, 20)
    stepList = uniqueRandList(3, 2, 5)
    for i in range(3):
        skipList.append(randint(0, lenList[i] - 1))
    taskList = []
    for i in range(3):
        taskList.append([lenList[i], startList[i], stepList[i], skipList[i]])
    return taskList


# takes list of 3 lists [length, startNum, step, skipIndex]
# returns list ['question', 'solution']
def taskProgression(opList, step):
    progLen = opList[step][0]
    start = opList[step][1]
    progStep = opList[step][2]
    skip = opList[step][3]

    progList = []
    nextNum = start
    for i in range(progLen):
        if i != skip:
            progList.append(str(nextNum))
        else:
            solutionLine = str(nextNum)
            progList.append('..')
        nextNum += progStep
    progLine = ' '.join(progList)
    return([progLine, solutionLine])


def inputValidate(inputStr):
    if inputStr.lstrip('-').isdigit():
        return True
    return False


def answerValidate(inputStr, solutStr):
    if inputStr == solutStr:
        return True
    return False


def main():
    print('Welcome to the Brain Games!')
    userName = welcome_user()
    promptLine = 'What number is missing in the progression?'
    brainGamesExec(userName, promptLine, taskInit, taskProgression,
                   inputValidate, answerValidate)


if __name__ == '__main__':
    main()
