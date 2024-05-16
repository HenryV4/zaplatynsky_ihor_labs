import unittest
from src.trie import Trie


class TestTrie(unittest.TestCase):


    
    def test_insert_and_search(self):
        self.trie = Trie()
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))
        self.assertFalse(self.trie.search("app"))
        self.assertFalse(self.trie.search("banana"))

    def test_start_with(self):
        self.trie = Trie()
        self.trie.insert("apple")
        self.trie.insert("app")
        self.assertTrue(self.trie.starts_with("app"))
        self.assertFalse(self.trie.starts_with("ban"))

    def test_starts_with_partial_word(self):
        self.trie = Trie()
        words = ["apple", "banana", "orange", "grape"]
        for word in words:
            self.trie.insert(word)
        self.assertTrue(self.trie.starts_with("banan"))
        self.assertTrue(self.trie.starts_with("grap"))
        self.assertFalse(self.trie.starts_with("oranee"))

if __name__ == '__main__':
    unittest.main()
