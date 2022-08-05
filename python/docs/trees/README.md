# Trees
Trees are very similar to a linked list however they have more than one next node.

[Binary Tree](../../data_structures/binary_tree.py)
[Binary Search Tree](../../data_structures/binary_search_tree.py)

## Challenge
This Code Challenge 15 required that I design my own tree and binary search tree class with `pre-order`, `in-order`, and `post-order` traversal methods for the tree and `add` and `contains` method for the binary search tree.

## Approach & Efficiency
I used recursion in all methods

### Traversals

- **Time** -> O(n) for all traversals since it has to look at every node in order print it.
- **Space** -> O(1) extra space required since the traversal happens in space and does not allocate any extra memory

### Add and Contains

- **Time** -> O(log(n)) for `contains` and `add` since the array is sorted and the search area for the location to find or add the value gets cut in half (approximately) with every node and operation.
- **Space** -> O(1) extra space required since the operations happens in space and do not allocate any extra memory (except `add` which allocates memory for one additional node)

![Linked List Whiteboard](White%20Board.png)
