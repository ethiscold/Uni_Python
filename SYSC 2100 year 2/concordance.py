"""
SYSC 2100 Winter 2024
Lab 1, Part 3, Exercise 4, Extra-Practice Exercise 5
"""

__author__ = 'Ethan Robitaille'
__student_number__ = '101233797'

import string

# For information about the string module, type help(string) at the shell
# prompt, or browse "The Python Standard Library", Section "Built-in Types",
# Subsection "Text Sequence Type - str" in the documentation
# (available @ python.org).


import string

# For information about the string module, type help(string) at the shell
# prompt, or browse "The Python Standard Library", Section "Built-in Types",
# Subsection "Text Sequence Type - str" in the documentation
# (available @ python.org).


def build_concordance(filename: str) -> dict[str, list[int]]:
    """Return a concordance of words in the text file with the specified filename."""
    with open(filename, "r") as infile:
        concordance = {}
        line_number = 1
        for line in infile:
            words = line.split()
            for word in words:
                word = word.strip(string.punctuation).lower()
                if word not in concordance:
                    concordance[word] = [line_number]
                elif line_number not in concordance[word]:
                    concordance[word].append(line_number)
            line_number += 1
    return concordance

# Extra-Practice: Exercise 5 Solution

if __name__ == '__main__':
    concordance = build_concordance('sons_of_martha.txt')
    print(concordance)
    # Write your solution to Extra-practice Exercise 5 here
