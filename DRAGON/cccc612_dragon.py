import sys

len_memo = [-1] * 51
def gen_len_memo():
    len_memo[0] = 1

    for i in xrange(1,51):
        len_memo[i] = len_memo[i - 1] * 2 + 2

def get_dragon_ch(dragon_str, gen, skip):
    if gen == 0:
        return dragon_str[skip]

    for ch in dragon_str:
        if ch == 'X' or ch == 'Y':
            if skip >= len_memo[gen]:
                skip -= len_memo[gen]
            elif ch == 'X':
                return get_dragon_ch('X+YF', gen - 1, skip)
            else:
                return get_dragon_ch('FX-Y', gen - 1, skip)
        elif skip > 0:
            skip -= 1
        else:
            return ch

gen_len_memo()
tc = int(raw_input())

for _ in xrange(tc):
    gen, start, length = map(int, raw_input().split())

    for i in xrange(length):
        sys.stdout.write(get_dragon_ch('FX', gen, start + i - 1))
    print('')
