# from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node
from data_structures.queue import Queue


def fizz_buzz_tree(tree):
    if tree is None:
        return None
    elif tree.root is None:
        return KaryTree()
    else:
        tree_queue = Queue()
        tree_queue.enqueue(tree.root)
        fizz_tree = KaryTree()
        fizz_tree.root = Node()
        fizz_tree_queue = Queue()
        fizz_tree_queue.enqueue(fizz_tree.root)
        while not tree_queue.is_empty():
            curr = tree_queue.dequeue()
            fizz_curr = fizz_tree_queue.dequeue()
            if curr.value % 15 == 0:
                fizz_curr.value = "FizzBuzz"
            elif curr.value % 5 == 0:
                fizz_curr.value = "Buzz"
            elif curr.value % 3 == 0:
                fizz_curr.value = "Fizz"
            else:
                fizz_curr.value = str(curr.value)
            for child in curr.children:
                tree_queue.enqueue(child)
                fizz_node = Node()
                fizz_curr.children.append(fizz_node)
                fizz_tree_queue.enqueue(fizz_node)
        return fizz_tree


if __name__ == "__main__":
    my_tree = KaryTree()
    my_tree.root = Node(3)
    print(my_tree.root.value)
    my_tree.root.children.append(Node(5))
    print(my_tree.root.children[0].value)
