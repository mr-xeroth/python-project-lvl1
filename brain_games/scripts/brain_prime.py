#!/usr/b:win/env python3
from ..cli import welcome_user
from ..core import brainGamesExec
from random import seed, randint


primeNumList = []


def primeListCalc(max):
    global primeNumList
    primeNumList.append(2)
    for i in range(3, max):
        divisionCount = 0
        for j in range(2, i - 1):
            if not i % j:
                divisionCount += 1
        if not divisionCount:
            primeNumList.append(i)


def uniqueRandList(count, min, max):
    rndList = []
    num = 0
    while len(rndList) < count:
        while not num or num in rndList:
            num = randint(min, max)
        rndList.append(num)
    return rndList


def taskInit():
    global primeNumList
    seed(None)
    primeListCalc(100)

    # ought to contain 1 prime number at least
    def inPrimeList(opList):
        for i in opList:
            if i in primeNumList:
                return True
        return False
    opList = []
    while not inPrimeList(opList):
        opList = uniqueRandList(3, 2, 100)
    return opList


# takes random numbers list [x, y, z]
# returns list ['question', 'solution']
def taskPrime(opList, step):
    global primeNumList
    if opList[step] in primeNumList:
        solutionLine = 'yes'
    else:
        solutionLine = 'no'
    questionLine = str(opList[step])
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
    promptLine = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    brainGamesExec(userName, promptLine, taskInit, taskPrime, inputValidate,
                   answerValidate)


if __name__ == '__main__':
    main()
