# Linked List Zip
Build a queue class implementing only two stacks under the hood.

[Pseudoqueues](../../code_challenges/stack_queue_pseudo.py)

## Challenge
This Code Challenge 11 requires that you design a class a queue with all the enqueue/dequeue methods using only two stacks under the hood.

## Approach & Efficiency

Enqueue
- **Time** -> O(1) because only constant time is needed for adding to a stack.
- **Space** -> O(1) additional space is required for adding single nodes.

Dequeue
- **Time** -> O(n) the data must be transferred between stacks twice.
- **Space** -> O(1) additional space is required because no additional nodes are created, they are only moved around.
