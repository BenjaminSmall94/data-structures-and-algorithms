# Trees
Trees are very similar to a linked list however they have more than one next node.

[Binary Tree](../../data_structures/binary_tree.py)
[Binary Search Tree](../../data_structures/binary_search_tree.py)

## Challenge
This Code Challenge 15 required that I design my own tree and binary search tree class with `pre-order`, `in-order`, and `post-order` traversal methods for the tree and `add` and `contains` method for the binary search tree.
Code Challenge 17 required us to extend our tree implementation in order to add a find max method

## Approach & Efficiency
I used recursion in all methods

### Traversals

- **Time** -> O(n) for all traversals since it has to look at every node in order print it.
- **Space** -> O(1) extra space required since the traversal happens in space and does not allocate any extra memory

### Find Max

- **Time** -> O(n) for all since we needed to traversal the tree and find the greatest value.
- **Space** -> O(1) extra space required since the traversal happens in space and does not allocate any extra memory, besides an int to track the greatest value.

### Add and Contains

- **Time** -> O(log(n)) for `contains` and `add` since the array is sorted and the search area for the location to find or add the value gets cut in half (approximately) with every node and operation.
- **Space** -> O(1) extra space required since the operations happens in space and do not allocate any extra memory (except `add` which allocates memory for one additional node)

## WhiteBoards

### No WhiteBoard Required for original tree assignment
![Linked List Whiteboard](White%20Board.png)

### White Board for Tree Max
![Linked List with Max](White%20Board2.png)
