# QUANTIZE problem
# Author: JeongminCha (cjm9236@me.com)

MAX_VAL = 987654321

class Quantizer:
    def __init__(self, seq, length_seq):
        self.length = length_seq
        self.p_sum = self.parital_sum(seq)
        self.p_squared_sum = self.partial_sqaured_sum(seq)
        self.memo = [[-1 for _ in range(10)] for _ in range(self.length)]

    def parital_sum(self, seq):
        p_sum = [0 for _ in range(self.length)]
        p_sum[0] = seq[0]
        for index in range(1, self.length):
            p_sum[index] = p_sum[index-1] + seq[index]
        return p_sum

    def partial_sqaured_sum(self, seq):
        return self.parital_sum([elem ** 2 for elem in seq])

    # Returns SSE (Sum of Squared Errors)
    def calc_sse(self, start, end):
        sum = self.p_sum[end]
        sq_sum = self.p_squared_sum[end]
        if start != 0:
            sum = sum - self.p_sum[start-1]
            sq_sum = sq_sum - self.p_squared_sum[start-1]
        avg = int (float(sum)/(end-start+1) + 0.5)
        return sq_sum - 2*avg*sum + avg*avg*(end-start+1)

    # Returns MSSE (Minimum Sum of Squared Errors) for executing the quantization.
    def quantize(self, start_idx, num_class):
        if start_idx == self.length:
            return 0
        if num_class == 0:
            return MAX_VAL
        msse = self.memo[start_idx][num_class - 1]
        if msse != -1:
            return msse

        msse = self.memo[start_idx][num_class - 1] = MAX_VAL
        for end_idx in range(start_idx, self.length):
            msse = min(msse, self.calc_sse(start_idx, end_idx) + self.quantize(end_idx+1, num_class-1))
            self.memo[start_idx][num_class-1] = msse
        return msse

if __name__ == "__main__":
    # 1. Input the number of test cases.
    test_case = int(raw_input())

    for case in range(test_case):
        input = map(int, raw_input().split(' '))
        (length_seq, num_class) = (input[0], input[1])

        # 3. Input the elements of the sequence.
        sorted_seq = sorted(map(int, raw_input().split(' ')))

        quantizer = Quantizer(sorted_seq, length_seq)
        result = quantizer.quantize(0, num_class)
        print(result)