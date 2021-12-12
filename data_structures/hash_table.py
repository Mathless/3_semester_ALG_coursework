import math
import time


class Node:
    def __init__(self, key, val):
        self.next = None
        self.key = key
        self.val = val


class List_for_hash_table:
    def __init__(self, node=None):
        self.head = node

    def add_node(self, node):
        current = self.head
        if current.key == node.key:
            raise KeyError
        while current.next is not None:
            current = current.next
            if current.key == node.key:
                raise KeyError
        current.next = node

    def deleteNode(self, key):

        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.key == key):
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while (temp is not None):
            if temp.key == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if (temp == None):
            return

        # Unlink the node from linked list
        prev.next = temp.next
        temp = None

    def get_val(self, key):
        val = None
        current = self.head
        while current is not None:
            if current.key == key:
                return current.val
            current = current.next
        return None

    def get_keys(self):
        current = self.head
        s = []
        while current is not None:
            s.append(current.key)
            current = current.next
        return s


class HashTable:



    def __init__(self, values=[]):
        self.size = 10
        self.counter = 0
        self.table = [None] * self.size
        for val in values:
            self.insert(val)

    def _hash_simple(self, key: int):
        return key % self.size

    def _python_hash(self, key):
        return hash(str(key)) % self.size

    def _mul_hash(self, key):
        return math.floor(self.size*(0.61803398*key % 1))

    def hash_custom(self, key):
        return self._python_hash(key)

    def insert(self, key, val=123):
        self.counter += 1
        index = self.hash_custom(key)
        list_on_index = self.table[index]
        if list_on_index == None:
            self.table[index] = List_for_hash_table(Node(key=key, val=val))
        else:
            list_on_index.add_node(Node(key=key, val=val))
        self.resize()

    def get(self, key):
        index = self.hash_custom(key)
        list_on_index = self.table[index]
        res_val = None
        current = list_on_index.head
        while current is not None:
            if current.key == key: res_val = current.val
            current = current.next
        return res_val

    def delete(self, key):
        index = self.hash_custom(key)
        list_on_index = self.table[index]
        list_on_index.deleteNode(key=key)
        self.resize()

    def resize(self):
        #start = time.time()
        alpha = self.counter / self.size
        if alpha >= 0.7: self.size *= 2
        elif alpha < 0.2: self.size //= 2
        else: return
        old_table = self.table
        self.table = [None] * self.size
        for list_i in old_table:
            if list_i is not None:
                current = list_i.head
                while current is not None:
                    self.insert(current.key, current.val)
                    current = current.next
        #print(time.time()-start)
    def keys(self):
        res = []
        for list in self.table:
            if list is not None: res.extend(list.get_keys())
        return res


if __name__ == "__main__":
    ht = HashTable(list(range(0, 10000)))
