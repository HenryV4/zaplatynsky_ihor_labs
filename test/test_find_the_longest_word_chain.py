import unittest
from src.find_the_longest_word_chain import longest_word_chain, read_file, write_output


class TestLongestWordChain(unittest.TestCase):

    def test_longest_word_chain(self):
        words1 = [
            "crates",
            "car",
            "cats",
            "crate",
            "rate",
            "at",
            "ate",
            "tea",
            "rat",
            "a",
        ]
        assert longest_word_chain(words1) == 6

        words2 = ["car", "cat", "bat", "ate", "rat"]
        assert longest_word_chain(words2) == 1

        words3 = ["book", "cook", "cook", "look", "loop"]
        assert longest_word_chain(words3) == 1

    def test_read_file(self):
        words_file = "resources/wchain.in"
        expected_words = [
            "crates",
            "car",
            "cats",
            "crate",
            "rate",
            "at",
            "ate",
            "tea",
            "rat",
            "a",
        ]
        assert read_file(words_file) == expected_words

    def test_write_output(self):
        max_chain_lengths = 5
        output_file = "resources/output.out"
        write_output(max_chain_lengths, output_file)
        with open(output_file, "r") as file:
            content = file.read().strip()
            assert content == str(max_chain_lengths)


if __name__ == "__main__":
    unittest.main()
