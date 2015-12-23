# JLIS problem (Joined Longest Increasing Subsequence)
# Author: JeongminCha (cjm9236@me.com)

from sys import maxint
minint = -maxint

seq_A = []
seq_B = []

# Returns element of sequence at specified index.
# If the index is unavailable, it returns absolute minimum value.
def element(seq, index):
    if index < 0:
        return minint
    else:
        return seq[index]

# Returns length of JLIS of two sequences.
def get_JLIS(index_A = -1, index_B = -1):
    length_JLIS = 2
    max_elem = max(element(seq_A, index_A), element(seq_B, index_B))

    for index in range(index_A + 1, len(seq_A)):
        if max_elem < seq_A[index]:
            length_JLIS = max(length_JLIS, 1 + get_JLIS(index, index_B))

    for index in range(index_B + 1, len(seq_B)):
        if max_elem < seq_B[index]:
            length_JLIS = max(length_JLIS, 1 + get_JLIS(index_A, index))

    return length_JLIS

if __name__ == '__main__':
    # 1. Input number of test cases.
    num_case = int(raw_input())

    for case in range(num_case):
        # 2. Input the numbers of elements of two sequences.
        nums = raw_input().split(' ')
        num_A = int(nums[0])
        num_B = int(nums[1])

        # 3. Input the elements of the sequences.
        seq_A = map(int, raw_input().split(' '))
        seq_B = map(int, raw_input().split(' '))

        print(get_JLIS() - 2)