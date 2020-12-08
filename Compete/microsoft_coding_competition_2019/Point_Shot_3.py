import math
import os
from collections import defaultdict
import string
from bisect import bisect_left

def inputFromSim(textFile):
    return input()


def inputFromText(textFile):
    return textFile.readline()

def solverMain(a_num_shots,a_shots,b_num_shots,b_shots):


    a_score = 0
    b_score = 0

    max_dif = -math.inf

    a_shots.sort()
    b_shots.sort()

    for i in a_shots:
        a_2_shots = bisect_left(a_shots, i)
        b_2_shots = bisect_left(b_shots, i)

        temp_a_score = a_2_shots*2+(a_num_shots-a_2_shots)*3
        temp_b_score = b_2_shots * 2 + (b_num_shots - b_2_shots) * 3
        score_dif = temp_a_score-temp_b_score

        if score_dif > max_dif:
            max_dif = score_dif

            a_score = temp_a_score
            b_score = temp_b_score

        elif score_dif == max_dif:
            if a_score < temp_a_score:
                a_score = temp_a_score
                b_score = temp_b_score

    for i in b_shots:
        a_2_shots = bisect_left(a_shots, i)
        b_2_shots = bisect_left(b_shots, i)

        temp_a_score = a_2_shots * 2 + (a_num_shots - a_2_shots) * 3
        temp_b_score = b_2_shots * 2 + (b_num_shots - b_2_shots) * 3
        score_dif = temp_a_score - temp_b_score

        if score_dif > max_dif:
            max_dif = score_dif

            a_score = temp_a_score
            b_score = temp_b_score

        elif score_dif == max_dif:
            if a_score < temp_a_score:
                a_score = temp_a_score
                b_score = temp_b_score

    #try only 2 points for b
    temp_d = b_shots[b_num_shots-1]+1
    a_2_shots = bisect_left(a_shots, temp_d)
    b_2_shots = b_num_shots

    temp_a_score = a_2_shots * 2 + (a_num_shots - a_2_shots) * 3
    temp_b_score = b_2_shots * 2 + (b_num_shots - b_2_shots) * 3
    score_dif = temp_a_score - temp_b_score

    if score_dif > max_dif:
        max_dif = score_dif

        a_score = temp_a_score
        b_score = temp_b_score

    elif score_dif == max_dif:
        if a_score < temp_a_score:
            a_score = temp_a_score
            b_score = temp_b_score

    return a_score,b_score

if __name__ == '__main__':

    x = inputFromSim
    mFile = None

    if "PYCHARM_HOSTED" in os.environ.keys():
        x = inputFromText
        script_dir = os.path.dirname(__file__)
        mFile = open(script_dir + "/testcase.txt", "r")

    a_num_shots = int(x(mFile))

    a_shots = list(map(int, x(mFile).split()))

    b_num_shots = int(x(mFile))

    b_shots = list(map(int, x(mFile).split()))

    a,b = solverMain(a_num_shots,a_shots,b_num_shots,b_shots)

    print("{} {}".format(a,b))



