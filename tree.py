"""
Binary preorder traversal tree
"""


class Node(object):

    def __init__(self, value):
        # constructor
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):

    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.pre_order_print(tree.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def pre_order_print(self, start, traversal):
        """
        Root -> Left -> Right
        """
        if start:
            traversal += (str(start.value) + "-")
            # recusive below
            traversal = self.pre_order_print(start.left, traversal)
            traversal = self.pre_order_print(start.right, traversal)
        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(tree.print_tree("preorder"))

"""

Output: 1-2-4-5-3-6-7-8
        1
      /   \
     /     \
    2       3
   / \     / \
  4   5   6   7
               \
                8
"""
