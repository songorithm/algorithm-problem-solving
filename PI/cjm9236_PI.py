# PI problem
# Author: JeongminCha (cjm9236@me.com)

# Returns True if all elements are same.
def is_all_same(seq):
    return all(cur == next for cur, next in zip(seq[:-1], seq[1:]))

# Returns True if the input sequence is
# monotonically decreasing or increasing by 1
def is_monotonic_by_one(seq):
    return all(next == cur+1 for cur, next in zip(seq[:-1], seq[1:])) \
        or all(next == cur-1 for cur, next in zip(seq[:-1], seq[1:]))

# Returns True if elements in input sequence are alternate.
def is_alternate(seq):
    # If an element and next of next one are always the same,
    # the sequence is alternate.
    return all(cur == next_next for cur, next_next in zip(seq[:-2], seq[2:]))

# Returns True if the input sequence is an arithmetical progression.
def is_ap(seq):
    return all((next-cur) == (cur-prev) for prev,cur,next in zip(seq[:-2],seq[1:-1],seq[2:]))

def calculate_cost(seq):
    if is_all_same(seq):
        return 1
    elif is_monotonic_by_one(seq):
        return 2
    elif is_alternate(seq):
        return 4
    elif is_ap(seq):
        return 5
    else:
        return 10

cache = [0 for _ in range(10001)]

def calculate_min_cost(seq):
    for unit in range(3,6):
        cache[unit] = calculate_cost(seq[0:unit])

    for idx in range(3,len(seq),3):
        for unit in range(3,6):
            next_idx = idx + unit;
            if next_idx > len(seq):
                break
            for next_unit in range(3,6):
                rest = next_idx - next_unit;
                if rest >= 3:
                    cost = cache[rest] + calculate_cost(seq[rest: next_idx])
                    if cache[next_idx] == 0:
                        cache[next_idx] = cost
                    else:
                        cache[next_idx] = min(cost, cache[next_idx])

    return cache[len(seq)]

if __name__ == "__main__":
    test_case = int(raw_input())

    for case in range(test_case):
        seq = map(int, list(raw_input()))
        result = calculate_min_cost(seq)
        print(result)