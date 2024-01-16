"""
SYSC 2100 Winter 2024
Lab 1, Part 2, Exercises 2 and 3
Case study: a function that uses Python's str, list, tuple set and dict
abstract data types.
"""

__author__ = 'Ethan Robitaille'
__student_number__ = '101233797'

import string

# For information about the string module, type help(string) at the shell
# prompt, or browse "The Python Standard Library", Section "Built-in Types",
# Subsection "Text Sequence Type - str" in the Python documentation
# (available @ python.org).


def build_histogram(filename: str) -> dict[str, int]:
    """Return a histogram of the words in the text file with the specified name.

    The histogram is a collection of counters. Each counter keeps track of the
    number of occurrences of one word.

    The histogram is stored in a dictionary.The keys are the words in the text
    file. The value associated with each key is the number of occurrences of
    that word.

    >>> hist = build_histogram('sons_of_martha.txt')
    >>> hist
    >>> len(hist)  # How many different words are in the file?
    """
    infile = open(filename, "r")
    hist = {}

    for line in infile:

        # Split each line into a list of words.
        # By default, the split method removes all whitespace; e.g.,
        # '  Hello,    world!   '.split() returns this list:
        #
        #    ['Hello,', 'world!']
        #
        # and not:
        #
        #    ['  Hello,', '    world!   ']
        #
        # Notice that the punctuation marks have not been removed.

        word_list = line.split()

        # For each word, first remove any leading or trailing punctuation,
        # then convert the the word to lower case.
        #
        # Examples:
        #  'Hello,'.strip(string.punctuation) returns 'Hello'.
        #  'Hello'.lower() returns 'hello'.

        for word in word_list:
            word = word.strip(string.punctuation).lower()

            # or,
            # word = word.strip(string.punctuation)
            # word = word.lower()

            # Increment the counter that counts the number of times
            # word is in the file.
            # Don't count any empty strings that are created when punctuation
            # marks are removed.
            # For example, if variable word is a hyphen, '-',
            # word.strip(string.punctuation) returns the empty string, ''.

            if word != '':
                count = hist.get(word, 0)  # get returns the current count of
                # the number of occurrences of word,
                # or 0 if word is not yet in the
                # dictionary.
                hist[word] = count + 1

            # or simply,
            # hist[word] = hist.get(word, 0) + 1

    return hist


def most_frequent_word(hist: dict[str, int]) -> tuple[str, int]:
    """Return a tuple containing the most frequently occurring word in the
    specified histogram (a dictionary of word/occurrence count pairs),
    along with its frequency.

    >>> hist = build_histogram('sons_of_martha.txt')
    >>> hist
    >>> len(hist)  # How many different words are in the file?
    >>> most_frequent_word(hist)  # Which word occurs most often?
    """
    frequency = -1
    for word in hist:
        if hist[word] > frequency:
            frequency = hist[word]
            most_frequent = word

    return (most_frequent, frequency)


def words_with_frequency(hist: dict[str, int], n: int) -> list[str]:
    """Returns a list of all words in histogram hist that occur with
    frequency n. The list is sorted in ascending order.

    >>> hist = build_histogram('sons_of_martha.txt')
    >>> words_with_frequency(hist, 1)  # Which words occur once in the file?
    >>> words_with_frequency(hist, 5)  # Which words occur five times?
    """
    word = []
    for i in hist:
        if hist[i] == n:
            word.append(i)
    word.sort()
    print('Words with a frequency of', n,':')
    return word

    # Write your code for Exercise 3 here.


if __name__ == '__main__':
    # Build and display a histogram of the distinct words in a file
    filename = 'sons_of_martha.txt'
    hist = build_histogram(filename)
    print('File', filename, 'contains', len(hist), 'distinct words')
    print('The histogram is:', hist)

    print('The most frequently occurring word is: ', most_frequent_word(hist)[0])
    print('# of occurrences: ', most_frequent_word(hist)[1])
    print(words_with_frequency(hist, 5))
    # Write your code for Exercise 2, Step 5, here.
