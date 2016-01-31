# -*- coding: utf8 -*-

def poly(remain, prev=None):
    global mm
    if remain == 0:
        return 1

    if mm[prev-1][remain-1]:
        return mm[prev-1][remain-1]

    case_sum = 0
    for cnt in range(1, remain+1):
        case = prev + (cnt - 1)  # 가진 정사각형으로 구할 수 있는 경우의 수
        next_case = poly(remain - cnt, cnt)
        case_sum += case * next_case

    mm[prev-1][remain-1] = case_sum

    return case_sum


if __name__ == '__main__':
    tc = int(raw_input())
    mm = [[0 for j in xrange(100 - i)] for i in xrange(100) if i > 0]

    for t in xrange(tc):
        square_cnt = int(raw_input())
        p_sum = range(square_cnt+1)

        for n in range(1, square_cnt+1):
            m = square_cnt - n
            p_sum[n] = poly(m, n)  # n 를 기준으로 아래오는 정사각형들의 조합의 수를 반환

        total_sum = sum(p_sum)

        if total_sum >= 10000000:
            print(total_sum % 10000000)
        else:
            print(total_sum)
