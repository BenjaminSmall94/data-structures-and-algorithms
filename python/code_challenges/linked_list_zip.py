from data_structures.linked_list import LinkedList


def zip_lists(a, b):
    curr_a = a.head
    curr_b = b.head
    new_linked_list = LinkedList()
    while curr_a is not None and curr_b is not None:
        print(curr_a.value)
        print(curr_b.value)
        new_linked_list.append(curr_a.value)
        new_linked_list.append(curr_b.value)
        curr_a = curr_a.next
        curr_b = curr_b.next
    while curr_a is not None:
        new_linked_list.append(curr_a.value)
        curr_a = curr_a.next
    while curr_b is not None:
        new_linked_list.append(curr_b.value)
        curr_b = curr_b.next
    return new_linked_list
