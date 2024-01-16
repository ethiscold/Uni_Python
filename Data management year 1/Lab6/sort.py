# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Ethan Robitaille, Rana Taunk, Prasidhaan Anandavimalan"

# Update "" with your team (e.g. T102)
__team__ = "T114"

#==========================================#
# Place your sort_students_age_bubble function after this line
def sort_students_age_bubble(input1:list,mode:str)->list:
    """
    Takes in a list of dictionarys and a string A or D and returns a sorted list 
    using bubble sort dictated by the key Age and is sorted by the input string.
    
    Preconditions:
    - Mode must be A or D
    - input1 must be atleast length 2
    - Key Age must be typed as is (caps matter)
    
    Examples:
    >>>sort_students_age_bubble([{"Age":10,"School":"GP"},{"Age":19,"School":"MS"}], "D")
    [{"Age": 19, "School":"MS"}, {"Age":10, "School":"GP"}]
    >>> sort_students_age_bubble([{"School":"GP"}, {"School":"MS"}], "D")
    "Age" key is not present.
    [{"School":"GP"}, {"School":"MS"}]
    """
    swap = True
    for i in range(len(input1)):
        if input1[i].get("Age") == None:
            print("One or more dictionaries do not have a key named 'Age'")
            return input1        
    while swap:
        swap = False
        for i in range(len(input1) -1):
            if input1[i]["Age"] > input1[i+1]["Age"]:
                input1[i], input1[i+1] = input1[i+1], input1[i]
                swap = True
    if mode == "A":
        return input1
    elif mode == "D":
        input1.reverse()
        return input1

#==========================================#
# Place your sort_students_time_selection function after this line
def sort_students_time_selection(input1:list,mode:str)->list:
    """
    Takes in a list of dictionarys and a string A or D and returns a sorted list 
    using selection sort dictated by the key StudyTime and is sorted by the input string.
    
    Preconditions:
    - Mode must be A or D
    - input1 must be atleast length 2
    - Key StudyTime must be typed as is (caps matter)
    
    Examples:
    >>> sort_students_time_selection ( [{"StudyTime":10.2,"School":"GP"}, {"StudyTime":19.1,"School":"MS"}], "D")
    [{"StudyTime": 19.1, "School":"MS"}, {"StudyTime":10.2, "School":"GP"}]
    >>>sort_students_time_selection([{"School":"GP"},{"School":"MS"}], "D")
    "StudyTime" key is not present
    [{"School":"GP"}, {"School":"MS"}
    """
    for i in range(len(input1)):
        if input1[i].get("StudyTime") == None:
            print("One or more dictionaries do not have a key named 'StudyTime'")
            return input1
    for i in range(len(input1)):
        min_idx = i
        for j in range(i + 1, len(input1)):
            if input1[min_idx]['StudyTime'] > input1[j]['StudyTime']:
                min_idx = j
                input1[i]['StudyTime'], input1[min_idx]['StudyTime'] = input1[min_idx]['StudyTime'], input1[i]['StudyTime']
    if mode == 'A':
        return input1
    elif mode == 'D':
        input1.reverse()
        return input1

#==========================================#
# Place your sort_students_g_avg_insertion function after this line
"""Returns a sorted list in ascending or descending order of student's 
dictionaires by "Failures" attribute. 

Preconditions: 
dict_student == "A" or sort_students == "D"

Examples:
>>>sort_students_g_avg_insertion( [{"G_Avg":7.2,"School":"GP"}, {"G_Avg":9.1,"School":"MS"}], "D")
[{'G_Avg': 9.1, 'School': 'MS'}, {'G_Avg': 7.2, 'School': 'GP'}]

>>>sort_students_g_avg_insertion( [{"G_Avg":7.2,"School":"GP"},
 {"G_Avg":9.1,"School":"MS"}, {"G_Avg":0.2,"School":"GP"}], "A")
[{'G_Avg': 0.2, 'School': 'GP'}, {'G_Avg': 7.2, 'School': 'GP'}, {'G_Avg': 9.1, 'School': 'MS'}]

>>>sort_students_g_avg_insertion( [{"G_Av":7.2,"School":"GP"},
 {"G_Advg":9.1,"School":"MS"}, {"G_Avg":0.2,"School":"GP"}], "A")
"G_Avg" key is not present

"""

def sort_students_g_avg_insertion(dict_student: list, char: str) -> list:
    if "G_Avg" not in dict_student[0]:
        dict_student('"G_Avg" key is not present')
        return

    for i in range(1, len(dict_student)):
        current = dict_student[i]

        if "G_Avg" not in current:
            print('"G_Avg" key is not present')
            return dict_student
    
        j = i - 1
        
        if char == 'A':
            while j >= 0 and current["G_Avg"] < dict_student[j]["G_Avg"]:
                dict_student[j + 1] = dict_student[j]
                j = j - 1
        else:
            while j >= 0 and current["G_Avg"] > dict_student[j]["G_Avg"]:
                dict_student[j + 1] = dict_student[j]
                j = j - 1


        dict_student[j + 1] = current


    return dict_student

#==========================================#
# Place your sort_students_failures_bubble function after this line
def sort_students_failures_bubble(studentlist: list, order: str)-> list:
    """
   Sort a list of students based on the "Failures" attribute using the bubble sort algorithm 
   
   Examples:
   >>>sort_students_failures_bubble([{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS"}], "D")
   [{'Failures': 19, 'School': 'MS'}, {'Failures': 10, 'School': 'GP'}]
   
   >>>sort_students_failures_bubble([{"Failures":9,"School":"BD"},{"Failures":18,"School":"GP"}], "A")
   [{'Failures': 9, 'School': 'BD'}, {'Failures': 18, 'School': 'GP'}]
   
   >>>sort_students_failures_bubble([{"School":"BD"}, {"School":"GP"}], "A")
   "Failures" key is not present.
   [{'School': 'BD'}, {'School': 'GP'}]

   
   """
    for i in range(len(studentlist)):
        if 'Failures' in studentlist[i]:
            continue
       
        else:
            print('"Failures" key is not present.')
            return studentlist   
   
    if order not in ["A", "D"]:
        raise ValueError("Order must be 'A' for ascending or 'D' for descending.")
    
    for i in range(len(studentlist)):
        for j in range(len(studentlist)-i-1):
            if studentlist[j].get("Failures", float("inf")) > studentlist[j+1].get("Failures", float("inf")):
                studentlist[j], studentlist[j+1] = studentlist[j+1], studentlist[j]
         
        
    if order == "D":
        studentlist = list(reversed(studentlist))
    
    return studentlist

#==========================================#
# Place your sort function after this line
def sort(input1:list,mode:str,atr:str)->list:
    """
    
    Preconditions:
    - Mode must be A or D
    - input1 must be atleast length 2
    - atr must be: Age, StudyTime, G_Avg, Failures
    
    Examples:
    >>>sort([{"Age":10,"School":"GP"},{"Age":19.1,"School":"MS"}],"D","Age")
    [{"Age": 19, "School":"MS"}, {"Age":10, "School":"GP"}]
    >>>sort([{"School":"GP"},{"School":"MS"}], "D", "School")
    Cannot be sorted by "School"
    [{"School":"GP"}, {"School":"MS"}]
    """
    if atr == "Age":
        return sort_students_age_bubble(input1,mode)
    elif atr == "StudyTime":
        return sort_students_time_selection(input1,mode)
    elif atr == "G_Avg":
        return sort_students_g_avg_insertion(input1,mode)
    elif atr == "Failures":
        return sort_students_failures_bubble(input1,mode)
    else:
        print("Cant be sorted by attribute " + atr)
        return input1
    
# Do NOT include a main script in your submission
