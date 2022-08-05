from data_structures.binary_tree import BinaryTree


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def add(self, value):
        def _add(value, tree_node):
            if value < tree_node.value:
                if tree_node.left is None:
                    tree_node.left = Node(value)
                else:
                    _add(value, tree_node.left)
            if value > tree_node.value:
                if tree_node.right is None:
                    tree_node.right = Node(value)
                else:
                    _add(value, tree_node.right)

        if self.root is None:
            self.root = Node(value)
        else:
            _add(value, self.root)

    def contains(self, value):
        def _contains(value, tree_node):
            if tree_node.value == value:
                return True
            elif tree_node.value < value:
                if tree_node.right is None:
                    return False
                else:
                    return _contains(value, tree_node.right)
            else:
                if tree_node.left is None:
                    return False
                else:
                    return _contains(value, tree_node.left)

        if self.root is None:
            return False
        else:
            return _contains(value, self.root)

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
