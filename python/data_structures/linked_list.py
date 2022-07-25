class LinkedList:
    """
    Defines class implementation of a linked list data structure with methods for prepending, appending, and inserting
    before and after a specified value
    """

    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(val)

    def insert_before(self, val, new_val):
        if self.head is None:
            raise TargetError
        elif self.head.value == val:
            temp = self.head
            self.head = Node(new_val, temp)
        else:
            curr = self.head
            while curr.next is not None:
                if curr.next.value == val:
                    curr.next = Node(new_val, curr.next)
                    break
                else:
                    curr = curr.next
            else:
                raise TargetError

    def insert_after(self, val, new_val):
        curr = self.head
        while curr is not None:
            if curr.value == val:
                curr.next = Node(new_val, curr.next)
                break
            else:
                curr = curr.next
        else:
            raise TargetError

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
    Defines a class that behaves as the node for singly linked list
    """
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class TargetError(Exception):
    pass
