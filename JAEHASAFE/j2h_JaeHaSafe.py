#!/usr/bin/python

class JaeHaSafe():
    def shiftLeft(self, inputList):
        r = inputList[1:]
        r.append(inputList[0])
        return r

    def shiftRight(self, inputList):
        r = inputList[:-1]
        r.insert(0, inputList[-1])
        return r

    def sameWhile(self, fromList, toList):
        _fromList = fromList[:]
        maxCnt = len(fromList)
        # Left
        cnt = 0
        for _ in range(maxCnt):
            _fromList = self.shiftLeft(_fromList)
            cnt = cnt + 1
            if _fromList == toList:
                break
        if maxCnt > cnt:
            return cnt
        # Right
        cnt = 0
        for _ in range(maxCnt):
            _fromList = self.shiftRight(_fromList)
            cnt = cnt + 1
            if _fromList == toList:
                break
        return cnt

    def solve(self, inputList):
        _inputList = []
        for _str in inputList:
            _inputList.append(list(_str))

        cnt = 0
        for idx in range(len(_inputList)-1):
            cnt = cnt + self.sameWhile(_inputList[idx], _inputList[idx+1])
        return cnt

if __name__ == '__main__':
    TC = int(raw_input())
    INDEX = 0
    answerList = []

    while INDEX < TC:
        numberOfList = int(raw_input())
        inputList = []
        for _ in range(numberOfList+1):
            inputList.append(raw_input())

        answerList.append(JaeHaSafe().solve(inputList))
        INDEX = INDEX + 1

    for answer in answerList:
        print(answer)
