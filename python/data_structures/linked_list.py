class LinkedList:
    """
    Put docstring here
    """

    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):
        curr = self.head
        while curr is not None:
            if curr.value == value:
                return True
            curr = curr.next

    def to_list(self):
        curr = self.head
        output = []
        while curr is not None:
            output.append(curr.value)
            curr = curr.next
        return output

    def __str__(self):
        curr = self.head
        output = ""
        while curr is not None:
            output += "{ " + str(curr.value) + " } -> "
            curr = curr.next
        output += "NULL"
        return output

class Node:
    """

    """
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class TargetError:
    pass
