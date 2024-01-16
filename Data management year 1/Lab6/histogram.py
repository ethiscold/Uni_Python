# ECOR 1042 Lab 6 - Individual submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Rana Taunk"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101258337"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-114"

#==========================================#
# Place your histogram function after this line

import numpy
import scipy
import matplotlib.pyplot as plt
#from import_data import *
#histogram([{"StudyTime":10.2,"School":"GP"}, {"StudyTime":19.1,"School":"MS"}], "StudyTime")
def histogram (diclist, strkey):
    values = [int((x[strkey])) // 1 for x in diclist]
    low = int(numpy.min(values))
    high = int(numpy.max(values))
    amount = []
    of = []

    if any(isinstance(x[strkey], float) for x in diclist):
        for n in range(int(low), int(high) + 1):
            amount.append(values.count(n))
            of.append("[" + str(n) + "-" + str(n + 1) + ")")

    else:
        for n in range(low, high + 1):
            amount.append(values.count(n))
            of.append(str(n))

    fig1 = plt.figure()
    plt.title(strkey + " Histogram")
    plt.xlabel(strkey + " Value")
    plt.ylabel("Count")
    plt.bar(of, amount, color='blue')
    plt.show()

# Do NOT include a main script in your submission
