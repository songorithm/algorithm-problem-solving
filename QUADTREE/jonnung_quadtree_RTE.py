# -*- coding: utf8 -*-
# Songorithm Season3 - Algorithm Problem Solving
#
# algostpot problem: QUADTREE
# date: 15/12/15
# author: jonnung <jonnung@gmail.com>


class QuadTree(object):
    def __init__(self):
        self.parent = None
        self.children = []
        self.r_children = []
        self.reverse_node = ''

    def add_child(self, node):
        if len(self.children) < 4:
            self.children.append(node)
        else:
            self.parent.add_child(node)

    def reverse_children(self):
        self.r_children = self.children[:]
        self.r_children[0], self.r_children[2] = self.r_children[2], self.r_children[0]
        self.r_children[1], self.r_children[3] = self.r_children[3], self.r_children[1]

        return 'x' + str.join('', [r.reverse_children() if isinstance(r, QuadTree) else r for r in self.r_children])


if __name__ == '__main__':
    test_case = int(raw_input())  # 입력1

    for tc in xrange(test_case):
        input_line = raw_input()  # 입력2

        if not input_line:
            print ''
            continue

        if input_line[0] != 'x':
            print(input_line[0])
            continue

        top_parent_node = None
        current_tree = None

        for char in input_line:
            if char == 'x':
                quad = QuadTree()
                if current_tree:
                    quad.parent = current_tree
                    current_tree.add_child(quad)
                else:
                    top_parent_node = quad
                current_tree = quad
            else:
                current_tree.add_child(char)

        print(top_parent_node.reverse_children())
