# ECOR 1042 Lab 4 - Individual submission for test2 function

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
__team__ = "T-114"

#==========================================#
#Do not modify the code alreayd provided.

def test_return_list_correct_lenght():
    #Complete the function with your test cases
    
    #test that student_school_list returns a list with the correct lenght (3 different test cases required)
    check.equal(len(student_school_list("student-test.csv", "A")), 0)
    check.equal(len(student_school_list("student-test.csv", "GP")), 3)
    check.equal(len(student_school_list("student-test.csv", "MS")), 4)
    
    #test that student_age_list returns a list  with the correct lenght (3 different test cases required)
    check.equal(len(student_age_list("student-test.csv", 16)), 2)
    check.equal(len(student_age_list("student-test.csv", 15)), 3)
    check.equal(len(student_age_list("student-test.csv", 7)), 0)    
    
    #test that student_health_list returns a list  with the correct lenght (3 different test cases required)
    check.equal(len(student_health_list("student-test.csv", 3)), 8)
    check.equal(len(student_health_list("student-test.csv", 5)), 3)
    check.equal(len(student_health_list("student-test.csv", 777)), 0)     
    
    #test that student_failures_list returns a list  with the correct lenght(3 different test cases required)
    check.equal(len(student_failures_list("student-test.csv", 0)), 11)
    check.equal(len(student_failures_list("student-test.csv", 3)), 1)
    check.equal(len(student_failures_list("student-test.csv", 400)), 0)     
    
    #test that load_data returns a list  with the correct lenght (6 different test cases required)
    check.equal(len(load_data("student-test.csv", ("ALL", -60))), 15) 
    check.equal(len(load_data("student-test.csv", ("school", "GP"))), 3)
    check.equal(len(load_data("student-test.csv", ("age", 15))), 3)
    check.equal(len(load_data("student-test.csv", ("health", 3))), 8)
    check.equal(len(load_data("student-test.csv", ("failures", 0))), 11)
    check.equal(len(load_data("student-test.csv", ("failures", 8))), 0)
    
    #test that add_average returns a list   with the correct lenght (3 different test cases required)
    check.equal(len(add_average([])), 0)
    check.equal(len(add_average(student_school_list("student-test.csv", "GP"))), 3)
    check.equal(len(load_data("student-test.csv", ("ALL", -60))), 15)
    
    check.summary()

# Do NOT include a main script in your submission
