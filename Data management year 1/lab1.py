# ECOR 1042 Lab 1

__author__ = "Ethan Robitaille"
__student_number__ = "101233797"

# ======================================================
# Exercise 1
"""
This fn takes a string and duplicates it based on how long the original string is
Parameter: String must be atleast 1 character
replicate("a")
>>>'a'
replicate("ab")
>>>'abab'
replicate("abc")
>>>'abcabcabc'
"""
final = ""
def replicate(s: str) -> str:
    for i in range(len(s)):
        if i == 0:
            final = s
        else:
            final += s
    return final
replicate("a")

# ======================================================
# Exercise 2
"""
This fn repeats a string n times and puts a divider string between replications
Parameters: n > 0, both strings must be minimum 1 character
repeat_separator("Word", "X", 3)
>>>"WordXWordXWord"
repeat_separator("This", "And", 2)
>>>"ThisAndThis"
repeat_separator("This", "And", 1) 
>>>"This"
"""
def repeat_separator(word:str, sep: str, n: int) -> str:
    for i in range(n):
        if i == 0:
            final = word
        else:
            final += sep + word
    return final
repeat_separator("Word", "X", 3)
# ======================================================
# Exercise 3
"""
This fn determines if a string has 2 characters in a row
Parameters: ch must be 1 character long s must be minimum 2 characters long
has_pair('abcdc', 'c')
>>>false
has_pair('abccd', 'c')
>>>true
has_pair('aabdc', 'a')
>>>true
"""
def has_pair(s:str,ch:str)->bool:
    for i in range(len(s)):
        if i == len(s)-1:
            return False
        else: 
            if s[i] + s[i+1] == ch+ch:
                return True    

# ======================================================
#PART B NO LOOPS
# Exercise 4
"""
This fn takes in 2 lists with 3 elements and returns the middle of both lists.
Parameters: Lists must 3 ints in length
middle_way([1, 2, 3], [4, 5, 6])
>>>[2,5]
middle_way([10, 87, 3], [4, 10002, 6])
>>>[87, 10002]
middle_way([10, 10, 3], [8, 4, 8])
>>>[10, 4]
"""
def middle_way(lst: list, kst: list)->list:
    final = []
    a=lst[round(len(lst)/2)-1]
    final.append(a)
    a=kst[round(len(kst)/2)-1]
    final.append(a)
    return final
# ======================================================
# Exercise 5
"""
This fn takes a list and returns the last and first character of the list
Parameter: input list must be atleast 2 elements in length
make_ends([4, 5, 6,7])
>>>[4,7]
make_ends([20, 5, 6,-10])
>>>[20,-10]
make_ends([-27, 5, 6,700])
>>>[-27, 700]
"""
def make_ends(lst:list)->list:  
    final = []
    final.append(lst[0])
    final.append(lst[-1])
    return final
# ======================================================
# Exercise 6
"""
This fn determines if they have the same first element or the same last 
element or if the first and last elements of both lists are the same
Parameters: lists must both have atleast one int
common_end([1, 2, 3], [1, 2])
>>>True
common_end([1], [1,2,1])
>>>True
common_end([7,8,2], [1,2,1])
>>>False
"""
def common_end(lst:list,kst:list)->bool:
    ai = lst[0]
    af = lst[-1]
    bi = kst[0]
    bf = kst[-1]
    if ai == bf:
        return True
    elif af == bi:
        return True
    elif ai == bi:
        return True
    elif af == bf:
        return True    
    else:
        return False
# ======================================================
#PART C no using built in list fns
# Exercise 7
"""
This fn counts how many even numbers there are in a list
Parameters: List must be of all ints and more than 1 int in length
count_evens([1, 23])
>>>0
count_evens([2,4,2,6,8,9])
>>>5
count_evens([2,5,6,7,8,9])
>>>3
"""
def count_evens(lst:list)-> int:
    a = 0
    for i in range(len(lst)):
        if lst[i]%2 == 0:
            a += 1
    return a

# ======================================================
# Exercise 8
"""
This fn returns the range of a list from the biggest and smallest number.
Parameter: list must have atleast 2 ints
big_diff([10, 3, 5, 6])
>>>7
big_diff([2,4])
>>>2
big_diff([2,4,6,1,7,10])
>>>9
"""
def big_diff(lst:list)->int:
    a = 0
    b = 999999999999999999999999999*9999999999999999999999999999999999999999999
    for i in range(len(lst)):
        if lst[i] < b:
            b = lst[i]
        if lst[i] > a:
            a = lst[i]
    return a - b
# ======================================================
# Exercise 9
"""
This fn determines if a list has 2 entrys of 2 back to back
Parameters: list must be all ints and atleast 2 ints in length
has22([1, 2, 2, 3])
>>>True
has22([1, 2, 4, 2])
>>>False
has22([2, 2, 4, 2])
>>>True
"""
def has22(lst:list)->bool:
    for i in range(len(lst)):
        if i == len(lst)-1:
            return False
        else: 
            if lst[i] + lst[i+1] == 4:
                return True

# ======================================================
# Exercise 10
"""
this fn returns the mean of a list of ints
Parameters: list must be atleast 3 characters in length and all ints
centered_average( [1, 1, 5, 5, 10, 8, 7])
>>>5.2
centered_average( [1, 6, 2, 87, 10, 3])
>>>5.25
centered_average( [10, 66, 24])
>>>24.0
"""
def centered_average(lst:list)->float:
    deleted = []
    a = 0
    lst.remove(max(lst))
    lst.remove(min(lst))
    print(lst)
    for i in range(len(lst)):
        a += lst[i]
    return a / len(lst)
# ======================================================
# Exercise 11
"""
This fn returns a list of total withdraws, deposits and value in a bank account
Parameters: input list must be atleast 1 element in length and a float value
bank_statement([-21.78, 14.69, 420.20, -278])
>>>[434.89, -299.78, 135.11]
bank_statement([12, -12, 1, -2])
>>>[13, -14, -1]
"""
def bank_statement(lst:list)->list:
    final = []
    a = 0
    b = 0
    c = 0
    for i in range(len(lst)):
        c += lst[i]
        if lst[i] > 0:
            a += lst[i]
        elif lst[i] < 0:
            b += lst[i]
            
    final.append(round(a,2))
    final.append(round(b,2))
    final.append(round(c,2))
    return final
# ======================================================
# Exercise 12
"""
This fn takes a list and reverses its contents
Parameter: list must be atleast 1 character in length
reverse([2,3])
>>>[3,2]
reverse([7,8,9,10])
>>>[10, 9, 8, 7]
reverse([4, 2, 3, 2])
>>>[2, 3, 2, 4]
"""
def reverse(lst:list)->list:
    final = []
    a = len(lst)
    for i in range(len(lst)):
        a -= 1
        final.append(lst[a])
    return final