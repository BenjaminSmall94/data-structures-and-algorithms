from data_structures.linked_list import LinkedList


class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024):
        self.buckets = [None] * size
        self.size = size

    def set(self, key, value):
        hashcode = self.hash(key)
        if self.buckets[hashcode] is None:
            self.buckets[hashcode] = LinkedList()
        bucket = self.buckets[hashcode]
        if bucket.head is not None:
            if bucket.head.value[0] == key:
                bucket.head = bucket.head.next
            else:
                prev = bucket.head
                drop = bucket.head.next
                while drop is not None:
                    if drop.value[0] == key:
                        prev.next = drop
                        break
                    prev = drop
                    drop = drop.next
        bucket.insert((key, value))

    def get(self, key):
        hashcode = self.hash(key)
        bucket = self.buckets[hashcode]
        if bucket is None:
            return None
        drop = bucket.head
        while drop is not None:
            if drop.value[0] == key:
                return drop.value[1]
            drop = drop.next
        return None

    def contains(self, key):
        hashcode = self.hash(key)
        bucket = self.buckets[hashcode]
        if bucket is None:
            return False
        drop = bucket.head
        while drop is not None:
            if drop.value[0] == key:
                return True
            drop = drop.next
        return False

    def keys(self):
        keys = []
        for bucket in self.buckets:
            if bucket is not None:
                drop = bucket.head
                while drop is not None:
                    keys.append(drop.value[0])
                    drop = drop.next
        return keys

    def hash(self, string):
        total = 0
        for char in string:
            total += ord(char)
        pre_mod_hash = total * 599
        return pre_mod_hash % self.size
