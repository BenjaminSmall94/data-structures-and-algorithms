# Linked List Insertions
Add functionality to your code through various additional functions.

## Challenge
This Code Challenge 4 required that I add the following methods to my code:

`append`
- arguments: new value
- adds a new node with the given value to the end of the list

`insert before`
- arguments: value, new value
- adds a new node with the given new value immediately before the first node that has the value specified

`insert after`
- arguments: value, new value
- adds a new node with the given new value immediately after the first node that has the value specified

## Approach & Efficiency
I used the iterative approach to work my way through the linked list to the desired location (whether that be the end or until a desire value)

- **Time** -> O(n) worst case for all operations because you would have to loop through the entire linked list in order to find the proper value.
- **Space** -> O(1) because only one pointer is needed regardless of the size of the linked list.

![Linked List Whiteboard](White%20Board.png)
