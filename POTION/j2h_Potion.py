#!/usr/bin/python

class Potion():
    def doSolve(self, n, p): # n: Ratio, p: Now input
        minRatio = self.getMinRatio(n)
        maxP = max(p)
        maxIdx = p.index(maxP)

        powerOf = maxP/minRatio[maxIdx]
        ratio = map(lambda x: powerOf*x, minRatio)

        while True:
            minIdx = ratio.index(min(ratio))
            if self.list1BiggerThenList2(ratio, p):
                return [a - b for a, b in zip(ratio, p)]
            else:
                powerOf = powerOf + 1
                ratio = map(lambda x: powerOf*x, minRatio)

    def list1BiggerThenList2(self, l1, l2):
        for idx in range(len(l1)):
            if l1[idx] < l2[idx]:
                return False
        return True

    def _getGCD(self, a, b): # Euclidean Algorithm
        while (b != 0):
            t = a%b
            a = b
            b = t
        return abs(a)

    def getGCD(self, l):
        gcd = l[:]
        while(len(gcd) > 1):
            first = gcd.pop()
            second = gcd.pop()
            gcd.append(self._getGCD(first, second))
        return gcd[0]

    def getMinRatio(self, l):
        gcd = self.getGCD(l)
        return map(lambda x: x / gcd, l)

if __name__ == '__main__':
    TC = int(raw_input())
    INDEX = 0
    answerList = []

    while INDEX < TC:
        raw_input() # skip
        n = [int(x) for x in raw_input().split(" ")]
        p = [int(x) for x in raw_input().split(" ")]
        answerList.append(Potion().doSolve(n, p))
        INDEX = INDEX + 1

    for answer in answerList:
        print(' '.join(str(p) for p in answer).strip())
