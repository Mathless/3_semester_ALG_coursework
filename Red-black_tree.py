class Node:
    def __init__(self, val=None, parent=None, color="black"):
        """constructor"""
        self.val = val
        self.parent = parent
        self._left = None
        self._right = None
        self.color = color

    # @property
    # def parent(self):
    #     return self._parent

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @left.setter
    def left(self, node):
        node.parent = self
        self._left = node

    @right.setter
    def right(self, node):
        node.parent = self
        self._right = node


class Tree:

    def __init__(self):
        self.node = None
