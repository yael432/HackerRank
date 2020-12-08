import math
import os

def inputFromSim(textFile):
    return input()


def inputFromText(textFile):
    return textFile.readline()

# /* Function to construct segment tree from given array.
# This function allocates memory for segment tree and
# calls constructSTUtil() to fill the allocated memory */
def constructSegmentTree(arr):
    height = int(math.ceil(math.log(len(arr)) / math.log(2)))
    size = 2 * int(math.pow(2, height)) - 1
    st = [0] * size;
    constructST(st, arr, 0, len(arr) - 1, 0);
    return st


# // A recursive function that constructs Segment
# // Tree for array[ss..se]. si is index of current
# // node in segment tree st

def constructST(st, arr, ss, se, si):
    if (ss == se):
        st[si] = int(arr[ss])
        return st[si]

    mid = int(ss + (se - ss) / 2)
    st[si] = int(gcd(constructST(st,arr, ss, mid, si * 2 + 1),
             constructST(st, arr, mid + 1, se, si * 2 + 2)))

    return st[si]

# // Function to find gcd of 2 numbers.
def gcd(a, b):
    if (a < b):
        # // If b greater than a swap a and b
        temp = b;
        b = a;
        a = temp;

    if (b == 0):
        return int(a)
    return int(gcd(b, a % b))


# // Finding The gcd of given Range
def findRangeGcd(st,ss, se, arr):
    n = len(arr)

    if (ss < 0 or se > n - 1 or ss > se):

        return int.MinValue;

    return findGcd(st,0, n - 1, ss, se, 0);

    # /* A recursive function to get gcd of given
    # range of array indexes. The following are parameters for
    # this function.
    #


# st --> Pointer to segment tree
# si --> Index of current node in the segment tree. Initially
# 		0 is passed as root is always at index 0
# ss & se --> Starting and ending indexes of the segment
# 			represented by current node, i.e., st[si]
# qs & qe --> Starting and ending indexes of query range */

def findGcd(st,ss, se, qs, qe, si):
    if (ss > qe or se < qs):
        return 0

    if (qs <= ss and qe >= se):
        return st[si];

    mid = int(ss + (se - ss) / 2)

    return gcd(findGcd(st,ss, mid, qs, qe, si * 2 + 1),
           findGcd(st,mid + 1, se, qs, qe, si * 2 + 2))


def mainSolver(arr,queries):

    for i in range(len(arr)):
        arr[i] = abs(arr[i])

    needToConstruct = True
    for q in queries:
        queryType, a, b = q[0],q[1],q[2]
        if queryType == 2:
            arr[a] = abs(b)
            needToConstruct = True
        else:
            if needToConstruct:
                st = constructSegmentTree(arr)
                needToConstruct = False
            print(findRangeGcd(st, a, b, arr))

if __name__ == '__main__':

    x = inputFromSim
    mFile = None

    if "PYCHARM_HOSTED" in os.environ.keys():
        x = inputFromText
        script_dir = os.path.dirname(__file__)
        mFile = open(script_dir + "/testcase.txt", "r")

    # a = [2, 3, 6, 9, 5]
    #
    # st = constructSegmentTree(a)
    #
    # l = 1
    # r = 3
    #
    # print("GCD of the given range is: ");
    # print(findRangeGcd(st, l, r, a))

    arr_size = int(x(mFile))
    arr = list(map(int, x(mFile).split()))
    steps = int(x(mFile))

    queries = []
    for i in range(steps):
        queryType, a, b = list(map(int, x(mFile).split()))
        queries.append((queryType, a, b))

    mainSolver(arr, queries)