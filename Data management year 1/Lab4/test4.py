# ECOR 1042 Lab 4 - Individual submission for test4 function

#import check module here
import check

#import load_data module here
import load_data
from load_data import student_school_list
from load_data import student_age_list
from load_data import student_health_list
from load_data import student_failures_list
from load_data import load_data
from load_data import add_average

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Ethan Robitaille"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101233797"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = ""

#==========================================#
#Do not modify the code alreayd provided.

def test_add_average():
    #Complete the function with your test cases
    
    #test that the function does not change the lengh of the list provided as input parameter (5 different test cases required)
    check.equal(len(add_average(student_school_list("student-test.csv", "GP"))), len(student_school_list("student-test.csv", "GP")))
    check.equal(len(add_average(student_age_list("student-test.csv", 18))), len(student_age_list("student-test.csv", 18)))
    check.equal(len(add_average(student_health_list("student-test.csv", 5))), len(student_health_list("student-test.csv", 5)))
    check.equal(len(add_average(student_failures_list("student-test.csv", 3))), len(student_failures_list("student-test.csv", 3)))
    check.equal(len(add_average(load_data("student-test.csv", ("ALL", -60)))), len(load_data("student-test.csv", ("ALL", -60))))
    
    #test that the function returns an empty list when it is called whith an empty list
    check.equal(len(add_average(student_school_list("student-test.csv", "A"))), 0)
    
    #test that the function inscrememnts the number of keys of the dictionary inside the list by one  (5 different test cases required)
    check.equal(len(add_average(student_school_list("student-test.csv", "GP"))[1].keys()), len(student_school_list("student-test.csv", "GP")[1].keys())+1)
    check.equal(len(add_average(student_age_list("student-test.csv", 18))[1].keys()), len(student_age_list("student-test.csv", 18)[1].keys())+1)
    check.equal(len(add_average(student_health_list("student-test.csv", 5))[0].keys()), len(student_health_list("student-test.csv", 5)[0].keys())+1)
    check.equal(len(add_average(student_failures_list("student-test.csv", 3))[0].keys()), len(student_failures_list("student-test.csv", 3)[0].keys())+1)
    check.equal(len(add_average(load_data("student-test.csv", ("School", 'GP')))[0].keys()), len(load_data("student-test.csv", ("School", 'GP'))[0].keys())+1)
    
    #test that the G_Avg value is properly calculated  (5 different test cases required)
    check.equal(add_average(student_school_list("student-test.csv", "GP"))[0]['G_Avg'], 5.67)
    check.equal(add_average(student_age_list("student-test.csv", 18))[2]['G_Avg'], 12.33)
    check.equal(add_average(student_health_list("student-test.csv", 5))[1]['G_Avg'], 4.33)
    check.equal(add_average(student_failures_list("student-test.csv", 3))[0]['G_Avg'], 8.33)
    check.equal(add_average(student_school_list("student-test.csv", "GP"))[2]['G_Avg'], 8.33)
   
    
    check.summary()

# Do NOT include a main script in your submission
