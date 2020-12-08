import math
import os
from collections import defaultdict
import string

def inputFromSim(textFile):
    return input()


def inputFromText(textFile):
    return textFile.readline()

def solverMain(N):

    #soltion:
    #https: // www.geeksforgeeks.org / number - of - different - cyclic - paths - of - length - n - in -a - tetrahedron /
    mod = 1e9+7


    # initially coming to B is B->B
    zB = 1

    # cannot reach A, D or C
    zADC = 0

    # iterate for all steps
    for i in range(1, N + 1):
        # recurrence relation
        nzB = zADC * 3

        nzADC = (zADC * 2 + zB)

        # memoize previous values
        zB = nzB
        zB %= mod
        zADC = nzADC
        zADC %= mod
        # returns steps
    return zB


if __name__ == '__main__':

    x = inputFromSim
    mFile = None

    if "PYCHARM_HOSTED" in os.environ.keys():
        x = inputFromText
        script_dir = os.path.dirname(__file__)
        mFile = open(script_dir + "/testcase.txt", "r")

    N = int(x(mFile))

    ans = solverMain(N)

    print("{}".format(int(ans)))



