# Cutting fence problem
# author: JeongminCha (cjm9236@me.com)

# stack with pair elements
# pair[0] = value, pair[1] = index
class PairStack(list):
    def __init__(self):
        self.items = []
    def push(self, item, index):
        self.items.append((item,index))
    def empty(self):
        return not self.items
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]

def cut_fence(fences):
    max_area = 0
    pre_fence = 0
    stack = PairStack()         # stack with pair elements

    for cur_index, cur_fence in enumerate(fences):
        new_index = cur_index
        # pop all fences with higher height than current fence's.
        while (stack.empty() == False and
               int(stack.peek()[0]) >= int(cur_fence)):
            max_area = max(max_area, int(stack.peek()[0]) * (cur_index - stack.peek()[1]))
            new_index = stack.pop()[1]
        # push current element with
        stack.push(cur_fence, new_index)

    return max_area

if __name__ == '__main__':
    test_case = int(raw_input())

    for case in range(test_case):
        num_fence = int(raw_input())        # number of fences
        fences = raw_input().split(' ')     # heights of fences
        fences.append(0)
        print(cut_fence(fences))