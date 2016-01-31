# NUMBERGAME problem
# Author: JeongminCha (cjm9236@me.com)
cache = None
seq = None

def optimal_score(left, right):
    if (right-left) == 0:
        return seq[left]
    elif (right-left) == 1:
        return abs(seq[left]-seq[right])

    found = cache[left][right]
    if found != -1:
        return found

    possible_score = [0] * 4
    possible_score[0] = seq[left] - optimal_score(left+1, right)
    possible_score[1] = seq[right] - optimal_score(left, right-1)
    possible_score[2] = 0 - optimal_score(left+2, right)
    possible_score[3] = 0 - optimal_score(left, right-2)

    mx = max(possible_score)
    cache[left][right] = mx
    return mx

if __name__ == "__main__":
    test_case = int(raw_input())

    for case in range(test_case):
        n = int(raw_input())
        seq = map(int, raw_input().split(' '))
        cache = [[-1]*n for _ in range(n)]

        result = optimal_score(0, n-1)
        print(result)
