class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binary_tree_diameter(root: BinaryTree):
    def height(el):
        null_el = -1
        if not el:
            return null_el
        return 1 + max(height(el.left), height(el.right))

    if not root:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)
    left_diameter = binary_tree_diameter(root.left)
    right_diameter = binary_tree_diameter(root.right)
    trough_the_root = left_height + right_height + 2
    return max(trough_the_root, left_diameter, right_diameter)
