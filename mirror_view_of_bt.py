
class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None


def mirror(node):
    if(node == None):
        return

    mirror(node.left)
    mirror(node.right)

    temp = node.left
    node.left = node.right
    node.right = temp


def inOrder(node):
    if (node == None):
        return

    inOrder(node.left)
    print(node.data, end=" ")
    inOrder(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inOrder(root)
print()
mirror(root)
print()
inOrder(root)