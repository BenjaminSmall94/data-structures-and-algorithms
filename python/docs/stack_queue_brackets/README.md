# Stack Queue Brackets
Build classes for stacks and queues

[Stack Queues Brackets](../../code_challenges/stack_queue_brackets.py)

## Challenge
This Code Challenge 12 requires that you take in a string as an argument and returns true or false if all the brackets in the string were properly closed.

## Approach & Efficiency
I iterated through the input string and used a stack to track opening braces and match them against closing braces

- **Time** -> O(n) because you always need to iterate through "n" elements of the string argument.
- **Space** -> O(n) space worst case because you might have a string full of opening braces in which case you would need to construct "n" new nodes on the stack.

![Linked List Whiteboard](White%20Board.png)
