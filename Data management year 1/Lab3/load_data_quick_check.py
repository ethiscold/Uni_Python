import unittest

from load_data import __author__, __team__, student_age_list, student_failures_list, student_health_list
from load_data import student_school_list, load_data, add_average


if __author__ == "":
    raise ValueError("_author__ was not assigned a string containing your name. Fix this.")

if __team__ == "":
    raise ValueError("__team__ was not assigned a string containing your student number. Fix this.")

age_list = student_age_list("student-mat.csv", 15)
failures_list = student_failures_list("student-mat.csv", 0)
health_list = student_health_list("student-mat.csv", 1)
school_list = student_school_list("student-mat.csv", 'GP')
all_list = load_data("student-mat.csv", ("All", 1))
with_avg = add_average(all_list)


print("All quick-checks pass. This just guarantee that you are meeting the minimum requirements.")
print("It is not testing the behavior of your function")
print("Make sure you have address the issues rised in the individual feedback")
print("Remember that no test scripts or interactive programs are permitted")
print("Also, make sure the function headers have type annotations.")
print("Make sure the docstrings are complete: function description, preconditions and examples.")




