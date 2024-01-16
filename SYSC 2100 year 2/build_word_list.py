"""
SYSC 2100 Winter 2024
Lab 1, Part 1, Exercise 1
Case study: a function that uses Python's str, list and set abstract
data types.
"""
import string
            
# For information about the string module
# - type help(string) at the shell prompt, or
# - read 'Practical Programming', Chapter 7, 'Using Methods'


def build_word_list(filename: str) -> list[str]:
    """Return a list of all the distinct words in the text file with the
    specified filename, sorted in ascending order.

    >>> word_list = build_word_list('sons_of_martha.txt')
    >>> word_list
    >>> len(word_list)  # How many different words are in the file?
    """
    # Algorithm: read a line from a text file and split the line into a
    # list of words. For each word in the list, remve any punctuation marks
    # before or after the word, convert the word to lower case, then put the
    # word in a set. (This is a simple way to discard duplicate words).
    # These steps are repeated until every line has been read and processed,
    # after which a new list is created, containing the words from the set.
    # The list is then sorted and returned.

    infile = open(filename, "r")
    word_set = set()

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

            # This statement is equivalent to:
            # word = word.strip(string.punctuation)
            # word = word.lower()

            # Store the word is the set.
            # Discard any empty strings that are created when punctuation
            # marks are removed.
            # For example, if variable word is a hyphen, '-',
            # word.strip(string.punctuation) returns the empty string, ''.

            if word != '':
                # Storing the words in a set discards any duplicates.
                word_set.add(word)

    # Now build the list of distinct words.
    word_list = list(word_set)

    # or,
    # word_list = []
    # for word in word_set:
    #    word_list.append(word)

    # Sort the list into ascending order.
    word_list.sort()

    return word_list


if __name__ == '__main__':
    filename = 'sons_of_martha.txt'
    word_list = build_word_list(filename)
    print('File', filename, 'contains', len(word_list), 'distinct words')
    print('The words are:', word_list)
