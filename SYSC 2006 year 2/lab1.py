# SYSC 2006 - Lab 1 Solution template

__author__ = "Ethan Robitaille"
__student_number__ = "101233797"

# Type your solution to exercise 1 after this line
def alarm_clock (day:int, vacation:bool) -> str:
    """
The function returns a string that indicates when the alarm will ring.
Preconditions: day must be between 0 and 6
alarm_clock(2,True)
>>>10:00
alarm_clock(4,False)
>>>7:00
alarm_clock(6,True)
>>>OFF
"""
    if day == 0 and vacation == True or day == 6 and vacation == True:
       return "off"
    elif day > 0 and day < 6 and vacation == True:
        return "10:00"
    elif day > 0 and day < 6 and vacation == False:
        return "07:00"
    elif day == 0 and vacation == False or day == 6 and vacation == False:
        return "10:00"
    else:
        return "Failed"

# Type your solution to exercise 2 after this line
def count_replace() -> str:
    """
The function returns a string that replaces any multiple of 3 with Fizz, a multiple of 5 with Buzz
and a multiple of both 3 and 5 with FizzBuzz.
Preconditions: input int must be positive
count_replace()
input 10
>>>1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz
count_replace()
input 20
>>>1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz
count_replace()
input 5
>>>1 2 Fizz 4 Buzz
"""
    a = ""
    number = int(input("Input an integer"))
    for i in range(number):
        if (i+1) % 3 == 0 and (i+1) % 5 ==0:
            a += "FizzBuzz "
        elif (i+1) % 3 == 0:
            a += "Fizz "
        elif (i+1) % 5==0:
            a += "Buzz "
        else:
            a += str(i+1) + " "
    print(a)

# Type your solution to exercise 3 after this line
def is_prime(num:int) -> bool:
    """
The function returns a boolean that indicates if the number is prime.
Preconditions: the integer must be positive
is_prime(8)
>>>False
is_prime(7)
>>>True
is_prime(9)
>>>False
"""
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Type your solution to exercise 4 after this line
def divisors(num:int) -> list:
    """
The function returns a list that contains all of the factors of the number.
Preconditions: the integer must be positive
divisors(16)
>>>[1, 2, 4, 8, 16]
divisors(25)
>>>[1, 5, 25]
divisors(9)
>>>[1, 3, 9]
"""
    a =[]
    for i in range (num):
        if num % (i + 1) == 0:
            a.append(i+1)
    return a