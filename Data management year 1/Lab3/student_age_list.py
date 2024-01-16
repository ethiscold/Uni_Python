# ECOR 1042 Lab 3 - Individual submission for student_age_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Ethan Robitaille"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101233797"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-114"

#==========================================#
# Place your student_age_list function after this line
import string
def student_age_list(name: str,age: int) -> list:
        file = open(name, 'r')
        header = []
        a = file.readline()
        header= a.strip().split(',')
        b = header[-1]
        c = b.split("\n")
        header[-1] = c[0]

        dic={}
        lst = []
        age = 18

        for row in file:
                csvreader= row.strip().split(',')
                for ch in range(len(csvreader)):
                        dic[header[ch]] = csvreader[ch]
                if int(csvreader[1]) == age:
                        a = dict.copy(dic)
                        a.pop('Age')
                        lst.append(a)  
        return lst
file.close()
                           

# Do NOT include a main script in your submission
