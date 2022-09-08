# Graph Business Trip

Develop an algorithm that checks to see if a particular route exists in a graph and returns the weight of the route if so.

[Breadth First Search](../../code_challenges/graph_business_trip.py)

## Challenge

Develop a method that checks to see if a particular route is possible in a graph

## Approach & Efficiency

- **Time** -> O(n * m) where n is the length of the route, and m is the average number of neighbors. Because for every stop on the route you have to construct a hash table with every neighbor.
- **Space** -> O(m) space because you copy every neighbor of the current node into a dictionary before resetting and doing it again.

![Linked List Whiteboard](White%20Board.png)
