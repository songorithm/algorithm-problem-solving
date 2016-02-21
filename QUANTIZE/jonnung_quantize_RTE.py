# -*- coding: utf8 -*-

if __name__ == '__main__':
    tc = int(raw_input())
    for t in range(tc):
        sequence_length, quantize_count = map(int, raw_input().split())
        n_sequence = map(int, raw_input().split())

        # n_seq를 정렬한다.
        n_sequence.sort()
        # print(n_sequence)

        # 정렬된 seq를 그룹화 한다.
        diff_sequence = [[i-1, i, n_sequence[i] - n_sequence[i-1]] for i in range(1, sequence_length)]
        diff_sequence.sort(None, key=lambda diff: diff[2], reverse=True)

        # print(diff_sequence)

        min_sum = 99999999999
        for q in range(quantize_count):
            grouping = []
            if not q:
                grouping.append(n_sequence)
            else:
                q_cut = diff_sequence[:q]
                q_cut.sort(None, key=lambda cut: cut[0])

                start = 0
                for c in range(q):
                    end = q_cut[c][1]
                    grouping.append(n_sequence[start:end])
                    start = end
                grouping.append(n_sequence[start:])

            # print(grouping)

            group_length = len(grouping)
            tmp_min = 0
            for g in range(group_length):
                avg = int(round(sum(grouping[g]) / float(len(grouping[g]))))

                for s in range(len(grouping[g])):
                    if avg > grouping[g][s]:
                        tmp_min += (avg - grouping[g][s])**2
                    else:
                        tmp_min += (grouping[g][s] - avg)**2

            if min_sum > tmp_min:
                min_sum = tmp_min

        print(min_sum)
