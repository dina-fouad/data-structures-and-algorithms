class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = node



    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return f'{values}'

##############################################

class Hashtable:

    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size


    def _hash(self, key):
        """
        Accepts the key and returns the index where this key should be stored
        """
        sum = 0
        for char in key:
            sum += ord(char)
        h = ( sum * 19) % self.size
        return h


    def add(self, key, value):
        index = self._hash(key)

        if not self._buckets[index]:
            self._buckets[index] = LinkedList()

        self._buckets[index].add([key, value])


    def find(self, key):
        """
        Accepts a key and returns the value for the key if it exists in our hashmap
        """
        index = self._hash(key)

        bucket = self._buckets[index]

        current = bucket.head
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next

        raise KeyError("Key not found", key)

    def delete(self, key):
        """
        Delete the value a the key
        """
        pass

    def contains(self, key):
        """
        Takes in the key and returns a boolean, indicating if the key exists in the table already.
        Args:
            key ([String]): [description]
        Returns:
            [bool]: [True if value exist, False if not]
        """

        idx = self._hash(key)
        bucket = self._buckets[idx]

        if bucket == None:
            return False

        current = bucket.head

        while current:

            if current.value['key'] == key:
                return True

            current = current.next
