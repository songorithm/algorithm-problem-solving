# -*- coding: utf8 -*-
# Songorithm Season3 - Algorithm Problem Solving
# https://github.com/songorithm/algorithm-problem-solving

# algostpot: QUADTREE
# date: 15/12/16
# author: jonnung <jonnung@gmail.com>

def reverse_quadtree(str_list):
    head = str_list.pop(0)

    if head != 'x':
        return head

    quad_list = [reverse_quadtree(str_list) for i in range(4)]

    quad_list[0], quad_list[2] = quad_list[2], quad_list[0]
    quad_list[1], quad_list[3] = quad_list[3], quad_list[1]

    return 'x' + str.join('', quad_list)


if __name__ == '__main__':
    test_case = int(raw_input())
    for tc in range(test_case):
        compression = list(raw_input())
        print(reverse_quadtree(compression))
