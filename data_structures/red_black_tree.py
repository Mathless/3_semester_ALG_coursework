class Node:

    def __init__(self, val=None, parent=None, color="black", left=None, right=None):
        """constructor"""
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
        self.color = color  # "red" or "black"


class Tree:

    def __init__(self, values = []):
        self.nil = Node()
        self.nil.color = "black"
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil
        for val in values:
            self.insert(val)



    def insert(self, new_val):
        x = self.root
        y = self.nil
        z = Node(val=new_val)
        while x != self.nil:
            y = x
            if z.val < x.val:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.val < y.val:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = "red"
        self._insert_fix(z)

    def _insert_fix(self, new_node):
        while new_node.parent.color == "red":
            if new_node.parent == new_node.parent.parent.left:
                uncle = new_node.parent.parent.right
                if uncle.color == "red":
                    new_node.parent.color = "black"
                    uncle.color = "black"
                    new_node.parent.parent.color = "red"
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self._left_rotate(new_node)
                    new_node.parent.color = "black"
                    new_node.parent.parent.color = "red"
                    self._right_rotate(new_node.parent.parent)
            else:
                uncle = new_node.parent.parent.left
                if uncle.color == "red":
                    new_node.parent.color = "black"
                    uncle.color = "black"
                    new_node.parent.parent.color = "red"
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self._right_rotate(new_node)
                    new_node.parent.color = "black"
                    new_node.parent.parent.color = "red"
                    self._left_rotate(new_node.parent.parent)
        self.root.color = "black"

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def find(self, val):
        return self._find_helper(self.root, val)

    def _transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete(self, val):
        node = self.find(val)
        if node != self.nil:
            self._delete(node)

    def _delete(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == "black":
            self._delete_fixup(x)

    def _find_helper(self, node, val):
        if node == self.nil:
            return node
        if node.val == val:
            return node
        if val > node.val:
            return self._find_helper(node.right, val)
        else:
            return self._find_helper(node.left, val)

    def _delete_fixup(self, x):
        while x != self.root and x.color == "black":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == "black" and w.right.color == "black":
                    w.color = "red"
                    x = x.parent
                else:
                    if w.right.color == "black":
                        w.left.color = "black"
                        w.color = "red"
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.right.color = "black"
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                if x == x.parent.right:
                    w = x.parent.left
                    if w.color == "red":
                        w.color = "black"
                        x.parent.color = "red"
                        self._right_rotate(x.parent)
                        w = x.parent.left
                    if w.right.color == "black" and w.left.color == "black":
                        w.color = "red"
                        x = x.parent
                    else:
                        if w.left.color == "black":
                            w.right.color = "black"
                            w.color = "red"
                            self._left_rotate(w)
                            w = x.parent.left
                        w.color = x.parent.color
                        x.parent.color = "black"
                        w.left.color = "black"
                        self._right_rotate(x.parent)
                        x = self.root
        x.color = "black"

    def _minimum(self, node=None):
        if node is None:
            node = self.root
        if self.root == self.nil:
            return self.nil
        while node.left != self.nil:
            node = node.left
        return node
