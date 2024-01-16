import unittest

from test2 import test_return_list_correct_lenght
from test2 import __author__, __student_number__, __team__

if __author__ == "":
    raise ValueError("_author__ was not assigned a string containing your name. Fix this.")
if __student_number__ == "":
    raise ValueError("__student_number__ was not assigned a string containing your name. Fix this.")
if __team__ == "":
    raise ValueError("__team__ was not assigned a string containing your student number. Fix this.")

test_return_list_correct_lenght()

print("Before this line you should see that the number of tests run is greater or equal to 21")
print("Some tests may pass, some test may fail")
print("***It is not testing the behavior of your function***")
print("If your replace the load_data file provided by your file, all test should pass")
print("Remember that no test scripts or interactive programs are permitted")




