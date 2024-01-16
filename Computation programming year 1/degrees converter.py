import math
import random

def convert_temp(C):
    """
    This function convert an input of celcius into kelvin
    
    Parameters : C temperature in degrees C
    
    >>> convert_temp(14)
    >>> 287
    
    >>> convert_temp(100)
    >>> 373
    
    >>> convert_temp(8)
    >>> 281
    """
    
    K =273+C
    return K

a = input("Please input a temperture in dgrees C")
a =int(a)
text = ("The degrees in K is " + str(convert_temp(a)))
print (text)