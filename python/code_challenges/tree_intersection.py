from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable


def tree_intersection(tree_a, tree_b):
    tree_a_vals = Hashtable()
    fill_tree_vals(tree_a.root, tree_a_vals)
    intersection = set()
    find_intersection(tree_b.root, tree_a_vals, intersection)
    return intersection


def find_intersection(node, a_vals, intersection):
    if node.left is not None:
        find_intersection(node.left, a_vals, intersection)
    if a_vals.contains(node.value):
        intersection.add(node.value)
    if node.right is not None:
        find_intersection(node.right, a_vals, intersection)


def fill_tree_vals(node, vals):
    if node.left is not None:
        fill_tree_vals(node.left, vals)
    vals.set(node.value, True)
    if node.right is not None:
        fill_tree_vals(node.right, vals)
