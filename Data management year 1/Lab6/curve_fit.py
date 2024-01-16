# ECOR 1042 Lab 6 - Individual submission for curve_fit function
from load_data import *
import matplotlib
import numpy
import scipy
import matplotlib.pyplot as plt
import numpy as np
# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Ethan Robitaille"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101233797"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-114"

#==========================================#
# Place your curve_fit function after this line
def curve_fit(input1:list, atr:str, deg:int):
    dict1  = {} 
    x = []
    y =[]
    b = []
    c=[]
    for i in range(len(input1)):
        if input1[i][atr] in dict1:
            dict1[input1[i][atr]] += [input1[i]["G_Avg"]]
        else:
            dict1[input1[i][atr]] = [input1[i]["G_Avg"]]
    for i in range(len(dict1)):
        counter = 0
        avg = 0
        keys = list(dict1.keys())
        for j in range(len(dict1[keys[i]])):
            avg += dict1[keys[i]][j]
            counter +=1
        avg=avg/counter
        dict1[input1[i][atr]] = [avg]
        y.append(avg)
        x.append(keys[i])
    if deg + 1 != len(y) or deg < len(y)-1:
        deg = len(y) -1 
    a = numpy.polyfit(x, y, deg)
    b = np.poly1d(a)
    print(b)
    c =str(b).split('\n')
    return c
    
# Do NOT include a main script in your submission