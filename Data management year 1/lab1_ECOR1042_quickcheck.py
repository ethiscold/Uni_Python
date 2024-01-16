# ECOR 1042 Lab 1 Quick-check
# Edited: Feb. 23, 2023;

# The import statements will trigger a ModuleNotFoundError if the name
# of the file containing the student's solutions is incorrect.
# An ImportError will be triggered if a function has an incorrect name.

from lab1 import __author__, __student_number__
from lab1 import replicate
from lab1 import repeat_separator
from lab1 import has_pair
from lab1 import middle_way
from lab1 import make_ends
from lab1 import common_end
from lab1 import count_evens
from lab1 import big_diff
from lab1 import has22
from lab1 import centered_average
from lab1 import bank_statement
from lab1 import reverse

# Check if the student has edited the statements that initialize
# __author__ and __student_number__.

if __author__ == "":
    raise ValueError("_author__ was not assigned a string containing your name. Fix this.")

if __student_number__ == "":
    raise ValueError("__student_number__ was not assigned a string containing your student number. Fix this.")


# Check if each function header has the correct number of parameters.
# The order of the parameters in the function headers is not checked.

result = replicate('abc')
result = repeat_separator("Word", "X", 3)
result = has_pair('abccd', 'c')
result = middle_way([1, 2, 3], [4, 5, 6])
result = make_ends([4, 5, 6, 7])
result = common_end([1, 2, 3], [1, 2])
result = count_evens([1, 23])
result = big_diff([10, 3, 5, 6])
result = has22([1, 2, 2, 3])
result = centered_average([6, 7, 4])
result = bank_statement([5.6, 7.7])
result = reverse([6, 7, 4])

print("All quick-checks pass.")
print("Before submitting lab1.py, check the function headers and")
print("verify that the order of the parameters is correct.\n")
print("Make sure your code follows 'The Rules' listed in the lab instructions:")
print("1. Parameter and local variable names must follow the naming conventions.")
print("2. No test scripts or interactive programs are permitted in lab1.py\n")
print("Also, make sure the function headers have descriptive parameter names and type annotations.")
print("Make sure the docstrings are complete: function description, preconditions and examples.")
