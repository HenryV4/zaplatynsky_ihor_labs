class Node:
    def __init__(self):
        self.letter = None
        self.is_end_of_word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Node()
            node = node.children[letter]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                return False
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return True
