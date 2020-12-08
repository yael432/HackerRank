import math
import os
from collections import defaultdict
import string

def inputFromSim(textFile):
    return input()


def inputFromText(textFile):
    return textFile.readline()

def solverMain(N):

    result = [0]*26

    for i in N:
        idx = string.ascii_lowercase.index(i)
        result[idx] = 1

    chrSum = sum(result)

    if chrSum%2 == 0:
        return "DOGE"
    else:
        return "BOT"


if __name__ == '__main__':

    x = inputFromSim
    mFile = None

    if "PYCHARM_HOSTED" in os.environ.keys():
        x = inputFromText
        script_dir = os.path.dirname(__file__)
        mFile = open(script_dir + "/testcase.txt", "r")

    N = x(mFile)

    ans = solverMain(N)

    print("{}".format(ans))



