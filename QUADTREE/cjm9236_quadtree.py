# Quadtree problem
# author: JeongminCha (cjm9236@me.com)

class node:
    children = []

    def __init__(self, compressed_string):
        self.children = []
        head = compressed_string.pop(0)
        if head != 'x':
            self.children.append(head)
        else:
            for iter in range(4):
                self.children.append(node(compressed_string))

    def is_complex(self):
        return 4 == len(self.children)

    def compression(self):
        compression_result = ''

        if self.is_complex() == True:
            compression_result = 'x'
        for child in self.children:
            if isinstance(child, node):
                compression_result += child.compression()
            else:
                compression_result += child

        return compression_result

    def reversed_child(self, index):
        child = self.children[index]

        if isinstance(child, node) == True:
            child.reverse()

        return child

    def reverse(self):
        if self.is_complex() == True:
            self.children[0], \
            self.children[1], \
            self.children[2], \
            self.children[3] \
                = \
            self.reversed_child(2), \
            self.reversed_child(3), \
            self.reversed_child(0), \
            self.reversed_child(1)

if __name__ == '__main__':
    test_case = int(raw_input())
    for case in range(test_case):
        compressed_string = list(raw_input())
        quad_tree = node(compressed_string)
        quad_tree.reverse()
        print (quad_tree.compression())

