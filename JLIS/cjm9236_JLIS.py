# JLIS problem (Joined Longest Increasing Subsequence)
# Author: JeongminCha (cjm9236@me.com)

from sys import maxint

len_A = 0
len_B = 0
seq_A = []
seq_B = []
JLIS = []

# Returns element of sequence at specified index.
# If the index is unavailable, it returns absolute minimum value.
def element(seq, index):
    if index < 0:
        return -maxint
    else:
        return seq[index]

# Returns length of JLIS of two sequences.
def get_JLIS(index_A = -1, index_B = -1):
    # Memoization
    length_JLIS = JLIS[index_A+1][index_B+1]
    if length_JLIS is not 0:
        return length_JLIS

    length_JLIS = 2

    max_elem = max(element(seq_A, index_A), element(seq_B, index_B))

    for index in range(index_A + 1, len_A):
        if max_elem < seq_A[index]:
            length_JLIS = max(length_JLIS, 1 + get_JLIS(index, index_B))

    for index in range(index_B + 1, len_B):
        if max_elem < seq_B[index]:
            length_JLIS = max(length_JLIS, 1 + get_JLIS(index_A, index))

    # Record a memo
    JLIS[index_A + 1][index_B + 1] = length_JLIS

    return length_JLIS

if __name__ == '__main__':
    # 1. Input number of test cases.
    num_case = int(raw_input())

    for case in range(num_case):
        # 2. Input the numbers of elements of two sequences.
        nums = raw_input().split(' ')
        len_A = int(nums[0])
        len_B = int(nums[1])

        # Initialize all elements of JLIS to -1.
        JLIS = [[int(0) for i in range(len_B + 1)] for j in range(len_A + 1)]

        # 3. Input the elements of the sequences.
        seq_A = map(int, raw_input().split(' '))
        seq_B = map(int, raw_input().split(' '))

        print(get_JLIS() - 2)