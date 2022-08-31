# Hash Table Left Join
Build an algorithm that merges two hash tables using left join logic.

[Hash Table Left Join](../../code_challenges/hashtable_left_join.py)

## Challenge
Develop an algorithm that merges two hash tables using left join logic.

## Approach & Efficiency
I used a depth first traversal to record all the value from the first tree in a hash set. I then used another depth first search to travers the second tree and find all the values in the second tree that were in the hash set from the first tree.

### Traversals

- **Time** -> O(n) time because you have to iterate through each tree once. First to find the values in the first, and then second to find the intersecting values in the second
- **Space** -> O(n) space because you are constructing a hash set of size equal to the original tree.


![Hash Table Left Join](White%20Board.png)
