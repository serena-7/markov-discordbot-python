"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()

    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    words = text_string.split()

    for i in range(len(words) - 2):
        pair = (words[i], words[i + 1])
        if pair in chains:
            chains[pair].append(words[i+2])
        else:
            chains[pair] = [words[i + 2]]

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    pair = choice(list(chains))

    while pair in chains:
        next_word = choice(chains[pair])
        words.append(next_word)
        pair = (pair[1], next_word)

    return ' '.join(words)
