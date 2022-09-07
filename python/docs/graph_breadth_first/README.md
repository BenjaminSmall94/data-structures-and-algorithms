# Graph Breadth First
Develop an algorithm that returns a list of Nodes in breadth first order

[Breadth First Search](../../data_structures/graph.py)

## Challenge
Develop a method that returns a list of node values saved in breadth first order

## Approach & Efficiency
I used a queue and a while loop to traverse through the graph. I used a hash set to keep track of which nodes had already been enqueued to avoid infinite loops that may be encountered in graphs.

### Traversals

- **Time** -> O(n) time because in order to save the new list you need to traverse through every item in the graph and copy it into the list
- **Space** -> O(n) space because you copy every item in the graph into the list


![Linked List Whiteboard](White%20Board.png)
