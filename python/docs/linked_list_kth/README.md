# Linked List kth Item from End of List
Add functionality to your code through various additional functions.

[Linked List implementation](../../data_structures/linked_list.py)

## Challenge
This Code Challenge 7 required that I add the following methods to my code:

`kth_from_end`
- arguments: integer representing distance from the end of the linked list
- returns the value of the node located k spaces away from the last node in the list

## Approach & Efficiency
I used the iterative method `to_list` to convert the linked list into an array. At that point I was able to grab the item k elements from the end. I considered adding reverse pointers and a tail pointer to solve this. Also I considered using recursion. But ultimately I went with the simplest implementation of using the `to_list` method.

- **Time** -> O(n) worst case for all operations because you would have to loop through the entire linked list in order to move the linked.
- **Space** -> O(n) because a whole new array of the same length of the linked list is created in solving this problem.

![Linked List Whiteboard](White%20Board.png)
