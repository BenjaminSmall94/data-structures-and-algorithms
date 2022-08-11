from data_structures.queue import Queue


class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self):
        self.root = None

    def pre_order(self):
        def _pre_order(tree_node):
            tree_vals.append(tree_node.value)
            if tree_node.left is not None:
                _pre_order(tree_node.left)
            if tree_node.right is not None:
                _pre_order(tree_node.right)

        tree_vals = []
        if self.root is not None:
            _pre_order(self.root)
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

    def find_maximum_value(self):
        def max_tree(tree_node):
            nonlocal maximum
            if tree_node.value > maximum:
                maximum = tree_node.value
            if tree_node.left is not None:
                max_tree(tree_node.left)
            if tree_node.right is not None:
                max_tree(tree_node.right)

        maximum = 0
        if self.root is not None:
            max_tree(self.root)
        return maximum

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            search_queue = Queue()
            search_queue.enqueue(self.root)
            while not search_queue.is_empty():
                curr = search_queue.dequeue()
                if curr.left is None:
                    curr.left = Node(value)
                    return
                else:
                    search_queue.enqueue(curr.left)
                if curr.right is None:
                    curr.right = Node(value)
                    return
                else:
                    search_queue.enqueue(curr.right)


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

if __name__ == "__main__":
    print("hi")
