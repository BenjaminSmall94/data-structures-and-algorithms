from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):
    tree_list = []
    search_queue = Queue()
    if tree is None:
        return tree_list
    if tree.root is not None:
        search_queue.enqueue(tree.root)
    i = 1
    while not search_queue.is_empty():
        curr = search_queue.dequeue()
        tree_list.append(curr.value)
        if curr.left is not None:
            search_queue.enqueue(curr.left)
        if curr.right is not None:
            search_queue.enqueue(curr.right)
        i += 1
    return tree_list
