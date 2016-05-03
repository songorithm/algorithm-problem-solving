# TRAVERSAL
# Jaekyoung Kim (rlakim5521@naver.com)

class Node:
    def __init__(self, key):
        self.key = key;
        self.left = None
        self.right = None

def makeTree(preorders, inorders):
    if(len(preorders) == 0):
        return None
    node = Node(preorders[0])
    slicePosition = inorders.index(preorders[0])
    node.left = makeTree(preorders[1:slicePosition+1], inorders[0:slicePosition])
    node.right = makeTree(preorders[slicePosition+1:], inorders[slicePosition+1:])
    return node

def postorderTraversal(node):
    if(node == None):
        return
    postorderTraversal(node.left)
    postorderTraversal(node.right)
    print node.key,

# Main function
if __name__ == "__main__":
    for _ in range(int(raw_input())):
        # Input
        # Number of node
        N = int(raw_input())
        # Preorder traversal case
        preorders = map(int, raw_input().split())
        # Inorder traversal case
        inorders = map(int, raw_input().split())
        
        # Solve
        root = makeTree(preorders, inorders)
        
        # Output
        postorderTraversal(root)
        print
