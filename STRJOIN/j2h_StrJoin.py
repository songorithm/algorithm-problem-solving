#!/usr/bin/python

class StrJoin():
    def calCostWithSortMethod(self, sortedList, sortMethod): # For Test
        totalCost = 0
        sortedList.sort()
        while len(sortedList) >= 2:
            sortedList = sortMethod(sortedList) # Custom
            firstMin = sortedList[0]
            secondMin = sortedList[1]
            cost = firstMin + secondMin
            totalCost = totalCost + cost
            sortedList = sortedList[2:]
            sortedList.append(cost)
        return totalCost

    def calCost(self, sortedList):
        totalCost = 0
        while len(sortedList) >= 2:
            sortedList.sort() # Default
            firstMin = sortedList[0]
            secondMin = sortedList[1]
            cost = firstMin + secondMin
            totalCost = totalCost + cost
            sortedList = sortedList[2:]
            sortedList.append(cost)
        return totalCost

if __name__ == '__main__':
    caseNum = int(input())
    answer = []
    for i in xrange(caseNum):
        n = int(input())
        inputList = map(int, raw_input().split())
        answer.append(StrJoin().calCost(inputList))

    while answer:
        print(answer.pop(0))
