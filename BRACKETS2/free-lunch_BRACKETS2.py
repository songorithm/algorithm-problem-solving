import sys

class Brackets2:
    def __init__(self, str):
        self.str = str
        self.bracketMap = {
            '(' : 0,
            '{' : 1,
            '[' : 2,
            ')' : 10,
            '}' : 11,
            ']' : 12,
        }

    def isValidated(self):
        stack = list()
        for c in self.str:
            if c != '\n':
                id = self.bracketMap.get(c)
                # CASE : Open Case
                if id < 10:
                    stack.append(id)
                # CASE : Close Case
                else :
                    # CASE : Stack is empty
                    if len(stack) == 0:
                        return False
                    # CASE : Mismatched Bracket
                    if stack.pop() + 10 != id:
                        return False
        # CASE : Remain open Brackets
        if len(stack) != 0:
            return False

        return True

if __name__ == "__main__":
    rl = lambda: sys.stdin.readline()
    retList = []
    for _ in xrange(int(rl())):
        input = rl()
        bracket = Brackets2(input)
        if bracket.isValidated():
            print "YES"
        else :
            print "NO"