class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self):
        self.root = None
        pass

    def pre_order(self):
        def _pre_order(tree_node, tree_vals):
            tree_vals.append(tree_node.value)
            if tree_node.left is not None:
                _pre_order(tree_node.left, tree_vals)
            if tree_node.right is not None:
                _pre_order(tree_node.right, tree_vals)

        tree_vals = []
        if self.root is not None:
            _pre_order(self.root, tree_vals)
        return tree_vals

    def in_order(self):
        def _in_order(tree_node, tree_vals):
            if tree_node.left is not None:
                _in_order(tree_node.left, tree_vals)
            tree_vals.append(tree_node.value)
            if tree_node.right is not None:
                _in_order(tree_node.right, tree_vals)

        tree_vals = []
        if self.root is not None:
            _in_order(self.root, tree_vals)
        return tree_vals

    def post_order(self):
        def _post_order(tree_node, tree_vals):
            if tree_node.left is not None:
                _post_order(tree_node.left, tree_vals)
            if tree_node.right is not None:
                _post_order(tree_node.right, tree_vals)
            tree_vals.append(tree_node.value)

        tree_vals = []
        if self.root is not None:
            _post_order(self.root, tree_vals)
        return tree_vals


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
