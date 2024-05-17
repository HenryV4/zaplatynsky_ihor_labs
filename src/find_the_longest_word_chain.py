def longest_word_chain(words):
    """Find the length of the longest word chain in a list of words.

    Args:
        words (list): A list of strings representing words.

    Returns:
        max_chain_lengths (int): The length of the longest word chain.
    """
    words.sort(key=lambda word: -len(word))

    max_chain_lengths = {word: 1 for word in words}

    for current_word in words:
        for j in range(len(current_word)):
            new_word = current_word[:j] + current_word[j + 1:]
            if new_word in max_chain_lengths:
                max_chain_lengths[new_word] = max(
                    max_chain_lengths[new_word], max_chain_lengths[current_word] + 1
                )

    return max(max_chain_lengths.values())


def read_file(file_path):
    """Reads words from a file.

    Args:
        file_path (str): The path to the input file.

    Returns:
        words (list): A list of strings representing words.
    """
    words = []
    with open(file_path, "r") as file:
        num_words = int(file.readline().strip())
        for _ in range(num_words):
            word = file.readline().strip()
            words.append(word)

    return words


def write_output(max_chain_lengths, file_path):
    """Writes the maximum chain lengths to a file.

    Args:
        max_chain_lengths (int): The maximum chain lengths.
        file_path (str): The path to the output file.

    """
    with open(file_path, "w") as file:
        file.write(str(max_chain_lengths))
