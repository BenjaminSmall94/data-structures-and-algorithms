from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError


class Stack:
    """
    Defines an implementation of a stack data structure.

    Contains all the common method s of push, pop, peek, and is_empty.
    """

    def __init__(self):
        self.top = None
        pass

    def push(self, value):
        new_node = Node(value, self.top)
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.value
        else:
            raise InvalidOperationError("Method not allowed on empty collection")

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            return self.top.value
