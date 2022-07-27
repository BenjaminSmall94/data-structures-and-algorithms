# Linked List Zip
Add functionality to your code through various additional functions.

[Linked List Zip Function](../../code_challenges/linked_list_zip.py)
[Linked List implementation](../../data_structures/linked_list.py)

## Challenge
This Code Challenge 8 requires that you design a function to zip tow linked lists together in alternating fashion:

- arguments: The heads of two linked lists
- returns a new linked list with the nodes of the input linked lists lined up in alternating fashion

## Approach & Efficiency
I used the iterative method  walk through every element in the input linked lists and copy them into a new linked list in alternating fashion and returned that linked list.

- **Time** -> O(n) because you have to loop through both linked lists in order to copy the values into the new list.
- **Space** -> O(n) because the new list is created of length equal to the sum of the lengths of the other two lists


![Linked List Whiteboard](White%20Board.png)
