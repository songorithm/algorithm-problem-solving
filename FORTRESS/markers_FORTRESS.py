# -*- encoding=utf-8 -*-
# author : markers
'''
  Created by Markers on 2016. 5. 04.
'''

import sys
import unittest

rl = lambda : sys.stdin.readline()


def sqrt(n):
    return n*n


class Test_FORTRESS(unittest.TestCase):
    def test_anything(self):
        pass


class Fortress():

    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
        self.children = []

    def __repr__(self):
        return "[ x = {}, y = {}, r = {} ]".format(self.x, self.y, self.r)

    def is_children(self,fortress):
        if sqrt(self.r - fortress.r) > self._distance(fortress):
            return True
        return False

    def _distance(self, fortress):
        return sqrt(self.x - fortress.x) + sqrt(self.y - fortress.y)

    def add_child(self,fortress):
        for child in self.children:
            if child.is_children(fortress):
                child.add_child(fortress)
                return
        self.children.append(fortress)

    def long_distance(self,m):
        if len(self.children) == 0:
            return 0

        m1 = 0
        m2 = 0
        for child in self.children:
            m2 = max(m2, child.long_distance(m) + 1)
            if m2 > m1:
                m2, m1 = m1 , m2
        m[0] = max(m[0], m1+m2)

        return m1


if __name__ == "__main__":

    for _ in xrange(int(rl().rstrip())):
        num_rampart = int(rl().rstrip())
        rampart_list = []
        for _ in xrange(num_rampart):
            x,y,r = map(int, rl().rstrip().split())
            rampart_list.append(Fortress(x,y,r))
        rampart_list.sort(key=lambda fortress: fortress.r,
                                   reverse=True)
        root = rampart_list.pop(0)

        for node in rampart_list:
            if root.is_children(node):
                root.add_child(node)

        m = [0]
        root.long_distance(m)
        print m[0]



"""
20 -> 10, 7, 5
10 -> 5, 2
7 -> 4
5 -> x
5 -> 3
2 -> x
4 -> x
"""