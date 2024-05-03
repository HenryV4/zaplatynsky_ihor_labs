class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.red = True
        self.parent = None
        self.left = None
        self.right = None


class RedBlackPriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        new_node = Node(value, priority)

        if not self.root:
            self.root = new_node
            new_node.red = False
            return

        parent = None
        current = self.root

        while current:
            parent = current
            if new_node.priority >= parent.priority:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if new_node.priority > parent.priority:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insertion(new_node)

    def fix_insertion(self, new_node):
        while new_node != self.root and new_node.parent.red == True:
            if new_node.parent == new_node.parent.parent.left:
                new_node = self.fix_insertion_left(new_node)
            else:
                new_node = self.fix_insertion_right(new_node)
        self.root.red = False

    def fix_insertion_left(self, new_node):
        uncle = new_node.parent.parent.right
        if uncle and uncle.red:  # colorflip
            uncle.red = False
            new_node.parent.red = False
            new_node.parent.parent.red = True
            new_node = new_node.parent.parent
        else:  # rotate
            if new_node == new_node.parent.right:
                new_node = new_node.parent
                self.left_rotate(new_node)
            new_node.parent.red = False
            new_node.parent.parent.red = True
            self.right_rotate(new_node.parent.parent)
        return new_node

    def fix_insertion_right(self, new_node):
        uncle = new_node.parent.parent.left
        if uncle and uncle.red:  # colorflip
            uncle.red = False
            new_node.parent.red = False
            new_node.parent.parent.red = True
            new_node = new_node.parent.parent
        else:  # rotate
            if new_node == new_node.parent.left:
                new_node = new_node.parent
                self.right_rotate(new_node)
            new_node.parent.red = False
            new_node.parent.parent.red = True
            self.left_rotate(new_node.parent.parent)
        return new_node

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def delete_max(self):
        if not self.root:
            return None

        current = self.root
        while current.left:
            current = current.left
        max_node = current

        if not max_node.parent:
            self.root = None
            return max_node.value

        if max_node.red:
            if max_node.left:
                max_node.parent.left = max_node.left
                max_node.left.parent = max_node.parent
            else:
                max_node.parent.left = None
                return max_node.value
        else:
            return self.delete_black_node(max_node)

    def delete_black_node(self, max_node):
        if max_node.left and max_node.left.red:
            max_node.parent.right = max_node.left
            max_node.left.parent = max_node.parent
            max_node.left.red = False
            return max_node.value
        if max_node.left:
            max_node.parent.right = max_node.left
            max_node.left.parent = max_node.parent
            self.fix_deletion(max_node)
        else:
            max_node.parent.right = None
            self.fix_deletion(max_node)

        return max_node.value

    def fix_deletion(self, node):
        while node != self.root and (node is not None and node.red == False):
            if node == node.parent.left:
                node = self.fix_deletion_left(node)
            else:
                node = self.fix_deletion_right(node)
        self.root.red = False

    def fix_deletion_left(self, node):
        sibling = node.parent.right
        if sibling and sibling.red == True:
            sibling.red = False
            node.parent.red = True
            self.left_rotate(node.parent)
            sibling = node.parent.right

        left_black = sibling.left is None or sibling.left.red == False
        right_black = sibling.right is None or sibling.right.red == False
        if left_black and right_black:
            sibling.red = True
            node = node.parent
        else:
            node = self.fix_deletion_left_case_2(node, sibling)
        return node

    def fix_deletion_left_case_2(self, node, sibling):
        if sibling.right is None or sibling.right.red == False:
            sibling.left.red = False
            sibling.red = True
            self.right_rotate(sibling)
            sibling = node.parent.right

        sibling.red = node.parent.red
        node.parent.red = False
        if sibling.right:
            sibling.right.red = False
            self.right_rotate(node.parent)
            node = self.root
        return self.root

    def fix_deletion_right(self, node):
        sibling = node.parent.left
        if sibling and sibling.red == True:
            sibling.red = False
            node.parent.red = True
            self.right_rotate(node.parent)
            sibling = node.parent.left

        right_black = sibling.right is None or sibling.right.red == False
        left_black = sibling.left is None or sibling.left.red == False

        if right_black and left_black:
            sibling.red = True
            node = node.parent
        else:
            node = self.fix_deletion_right_case_2(node, sibling)
        return node

    def fix_deletion_right_case_2(self, node, sibling):
        if sibling.left is None or sibling.left.red == False:
            sibling.right.red = False
            sibling.red = True
            self.right_rotate(sibling)
            sibling = node.parent.left
        sibling.red = node.parent.red
        node.parent.red = False
        if sibling.left:
            sibling.left.red = False
            self.right_rotate(node.parent)
            node = self.root

    def print_tree(self, node, level=0, prefix=""):
        if node and node.red == True:
            color = "RED"
        else:
            color = "BLACK"
        if node is not None:
            if node.right is not Node:
                self.print_tree(node.right, level + 1, "┌───")
            print(" " * (level * 4) + prefix + f"{node.value} {color} {node.priority}*")
            if node.left is not None:
                self.print_tree(node.left, level + 1, "└───")
