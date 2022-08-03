from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError


class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.front = None
        self.rear = None
        pass

    def enqueue(self, value):
        new_node = Node(value)
        if(self.is_empty()):
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            popped_node = self.front
            if self.front is self.rear:
                self.rear = None
            self.front = self.front.next
            popped_node.next = None
            return popped_node.value
        else:
            raise InvalidOperationError

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            return self.front.value

    def is_empty(self):
        return self.front is None
        pass

    def __str__(self):
        temp = Queue()
        string_rep = "Front -> "
        while not self.is_empty():
            curr = self.dequeue()
            string_rep += f"{curr} -> "
            temp.enqueue(curr)
        self = temp
        return string_rep
