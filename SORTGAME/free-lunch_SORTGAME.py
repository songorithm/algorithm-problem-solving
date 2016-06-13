import sys
import collections


def reverse_sublist(s,start,end):
    ret = str(s)
    ret = ret[:start]+ret[start:end+1][::-1]+ret[end+1:]
    return ret

distance = dict()
def preCalc(n):
    global distance
    perm = '01234567'[:n]

    q = collections.deque()
    q.append(perm)
    distance[perm] = 0

    while(len(q)):
        here = q.popleft()
        cost = distance[here]
        for i in xrange(n):
            for j in xrange(i+1, n):
                rvs_list = reverse_sublist(here, i, j)
                if not rvs_list in distance:
                    distance[rvs_list] = cost+1
                    q.append(rvs_list)
    #Finish

def covert_list(lst):
    sorted_list = list(lst)
    ret = []
    sorted_list.sort()

    for i in lst:
        ret.append(sorted_list.index(i))
    return ''.join(map(str,ret))

def solve(input):
    preCalc(len(input))
    return distance[covert_list(input)]

if __name__ == "__main__":

    rl = lambda: sys.stdin.readline()
    inputList = []

    for _ in xrange(int(rl())):
        rl()
        input =  map(int, rl().split(' '))
        inputList.append(covert_list(input))

    counter = collections.Counter()
    for input in inputList:
        counter[len(input)] = len(input)


    for i in counter:
        preCalc(i)

    for input in inputList:
        print(distance[input])
