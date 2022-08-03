from data_structures.queue import Queue


class AnimalShelter:

    def __init__(self):
        self.animal_queue = Queue()

    def enqueue(self, animal):
        self.animal_queue.enqueue(animal)

    def dequeue(self, pref):
        if pref == "dog":
            if isinstance(self.animal_queue.peek(), Dog):
                return self.animal_queue.dequeue()
            else:
                return self.check_queue(Dog)
        elif pref == "cat":
            if isinstance(self.animal_queue.peek(), Cat):
                return self.animal_queue.dequeue()
            else:
                return self.check_queue(Cat)
        else:
            return None

    def check_queue(self, animal_type):
        temp = Queue()
        return_val = None
        found = False
        while not self.animal_queue.is_empty():
            if isinstance(self.animal_queue.peek(), animal_type) and not found:
                return_val = self.animal_queue.dequeue()
                break
            temp.enqueue(self.animal_queue.dequeue())
        self.animal_queue = temp
        return return_val


class Animal:

    def __init__(self, animal_name="Animal"):
        self.name = animal_name

    def __str__(self):
        return self.name

class Dog(Animal):

    def __init__(self, animal_name="Doggy"):
        self.name = animal_name


class Cat(Animal):

    def __init__(self, animal_name="Kitty"):
        self.name = animal_name
