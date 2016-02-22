import sys
from operator import itemgetter

def lunchBox(list):
    # The index 0 of lunchbox is microwaving time
    # The index 1 of lunchbox is eating time
    sortedList = sorted(list, key=itemgetter(1), reverse=True)

    cusumMicrowaving = 0
    finishLunch = 0

    for lunchbox in sortedList:
        cusumMicrowaving += lunchbox[0]
        finishEating = cusumMicrowaving + lunchbox[1]
        finishLunch =  finishEating if finishEating > finishLunch else finishLunch

    return finishLunch

if __name__ == "__main__":
    inputList = []
    rl = lambda: sys.stdin.readline()

    for _ in xrange(int(rl())):
        rl()
        inputList.append(zip(map(int, rl().split()),map(int, rl().split())))

    for testcase in inputList:
        print lunchBox(testcase)