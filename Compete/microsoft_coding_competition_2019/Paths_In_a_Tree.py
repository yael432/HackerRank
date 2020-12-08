import os
from collections import defaultdict


def inputFromSim(textFile):
    return input()


def inputFromText(textFile):
    return textFile.readline()


def getsum2():

    #solution
    #https://codereview.stackexchange.com/questions/135915/sum-of-all-paths-between-all-pairs-of-nodes-in-a-tree

    tree_2 = defaultdict(list)
    nodes_count = defaultdict(int)

    # Number of vertices
    n = int(x(mFile))

    ans = 0

    for i in range(n - 1):
        m = x(mFile)

        a, b, w = list(map(int, m.split()))
        tree_2[a].append((b,w))
        tree_2[b].append((a,w))
        nodes_count[a] = 1
        nodes_count[b] = 1

    while len(tree_2):
        for i in tree_2.keys():
            if len(tree_2[i]) == 1:
                w = tree_2[i][0][1]
                ans += nodes_count[i]*(n-nodes_count[i])*w
                nextNode = tree_2[i][0][0]
                tree_2[nextNode].remove((i,w))

                nodes_count[nextNode] += nodes_count[i]
                del tree_2[i]
                if len(tree_2[nextNode]) == 0:
                    del tree_2[nextNode]
                break
    return ans


if __name__ == '__main__':

    x = inputFromSim
    mFile = None

    if "PYCHARM_HOSTED" in os.environ.keys():
        x = inputFromText
        script_dir = os.path.dirname(__file__)
        mFile = open(script_dir + "/testcase.txt", "r")


    ans = getsum2()

    print("{}".format(ans))
