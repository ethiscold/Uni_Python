# ECOR 1042 Lab 5 - Individual submission for sort_students_time_selection function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Ethan Robitaille"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101233797"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-114"

#==========================================#
# Place your sort_students_time_selection function after this line
def sort_students_time_selection(input1:list,mode:str)->list:
    """
    Takes in a list of dictionarys and a string A or D and returns a sorted list 
    dictated by the key StudyTime and is sorted by the input string.
    
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
# Do NOT include a main script in your submission
