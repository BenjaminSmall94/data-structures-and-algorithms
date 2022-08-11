# Tree Fizz Buzz
Develop an algorithm that plays the fizz buzz game with a k-ary tree.

[Breadth First Search](../../code_challenges/tree_fizz_buzz.py)

## Challenge
Develop a function that takes a k-ary tree and returns a new tree with the same structure but the values of its nodes have been replaced according to standard fizz buzz logic.

## Approach & Efficiency
I used a breadth first traversal to iterate through and copy all the values of the tree into a new one

### Traversals

- **Time** -> O(n) time because you have to iterate through every list in the node in order to make the new modified tree.
- **Space** -> O(n) space because you are constructing a new tree of size equal to the original tree


![Linked List Whiteboard](White%20Board.png)
