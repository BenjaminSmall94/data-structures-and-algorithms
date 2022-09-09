# Depth First Traversal
Conducting a depth first traversal in a graph is a little different than conducting a depth first traversal on a tree because you have to account for possible cycles by maintaining a visited hash set.

## Challenge
Write a method for your existing graph implementation that traverses through a graph in depth first pre-order fashion and then returns a list of nodes values in this ordere.

## Approach & Efficiency
I used recursion to traverse through the graph using the call stack in O(n) time. This would be O(n) worst case memory in the instance of a graph that really was a linked list (a single long path)
