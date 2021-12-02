class Node:
    def __init__(self, key, val):
        self.next = None
        self.key = key
        self.val = val


class List_imp:
    def __init__(self, node=None):
        self.head = node
        self.end = node

    def add_node(self, node):
        self.end.next = node
        self.end = node

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
        if temp == self.end:
            self.end = prev
        temp = None

    def get_val(self, key):
        val = None
        current = self.head
        while current is not None:
            if current.key == key:
                return current.val
            current = current.next
        return None

    def print(self):
        current = self.head
        s = ""
        while current is not None:
            s += " " + str(current.val)
            current = current.next
        print(s)


class HashTable:
    def __init__(self, values=[]):
        self.size = 10
        self.counter = 0
        self.table = [None] * self.size
        for val in values:
            self.insert(val)

    def hash_simple(self, key: int):
        return key % self.size

    def insert(self, key, val=123):
        self.counter += 1
        index = self.hash_simple(key)
        list_on_index = self.table[index]
        if list_on_index == None:
            self.table[index] = List_imp(Node(key=key, val=val))
        else:
            list_on_index.add_node(Node(key=key, val=val))
        if self.counter * 1.3 >= self.size: self.resize()

    def get(self, key):
        index = self.hash_simple(key)
        list_on_index = self.table[index]
        res_val = None
        current = list_on_index.head
        while current is not None:
            if current.key == key: res_val = current.val
            current = current.next
        return res_val

    def delete(self, key):
        index = self.hash_simple(key)
        list_on_index = self.table[index]
        list_on_index.deleteNode(key=key)

    def resize(self):
        old_table = self.table
        self.size = self.size**2
        self.table = [None] * self.size
        for list_i in old_table:
            if list_i is not None:
                current = list_i.head
                while current is not None:
                    self.insert(current.key, current.val)
                    current = current.next


if __name__ == "__main__":
    ht = HashTable()
    ht.insert(10, 100)
    ht.insert(20, 200)
    ht.insert(10, 100)
    ht.insert(20, 200)
    ht.insert(10, 100)
    ht.insert(20, 200)
    ht.insert(10, 100)
    ht.insert(20, 200)
    ht.insert(10, 100)
    ht.insert(20, 200)
    ht.insert(10, 100)
    ht.insert(20, 200)
    ht.insert(10, 100)
    ht.insert(20, 200)
    ht.insert(10, 100)
    ht.insert(20, 200)
