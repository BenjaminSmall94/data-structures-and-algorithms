# Linked List Zip
Build classes for stacks and queues

[Stacks](../../data_structures/stack.py)
[Queues](../../data_structures/queue.py)

## Challenge
This Code Challenge 10 requires that you design a class defining stacks and queues with all their required behavior.

## Approach & Efficiency
I used the iterative method  walk through every element in the input linked lists and copy them into a new linked list in alternating fashion and returned that linked list.

- **Time** -> O(1) for all operations because only constant time is needed for all common stack and queue methods.
- **Space** -> O(1) additional space is required for all operations of adding or removing single nodes.
