# Animal Shelter
Build a class that simulates an animal shelter with people dropping off animals and also coming to pick them up implementing a modified first in first out heuristic.

[Animal Shelter](../../code_challenges/stack_queue_animal_shelter.py)

## Challenge
This Code Challenge 12 requires that you design a class that simulates an animal shelter with the following method.

- Enqueue
   - Arguments: Animal (Dog or Cat)

- Dequeue
  - Arguments: Preference (Dog or Cat)
  - Returns the first available dog or cat from the queue based on the preference argument

## Approach & Efficiency

Enqueue
- **Time** -> O(1) because animals are always added to the rear of the queue.
- **Space** -> O(1) because only one new node is made.

Dequeue
- **Time** -> O(n) worst case since the queue will have to be iterated through to remove a middle indexed item and them reconstruct the queue.
- **Space** -> O(0) because no new data is created with this operation.
