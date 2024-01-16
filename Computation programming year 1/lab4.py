# ECOR 1041 Lab 4

__author__ = "Ethan Robitaille"
__student_number__ = "101233797"

import math

# =====================================================
# Exercise 1
def area_of_disk(radius: float) -> float:
  """
  Return the area of a disk with the specified radius.
  Precondition: radius >= 0.
  >>>area_of_disk(5)
  78.54
  >>>area_of_disk(25)
  1963.50
  >>>area_of_disk(100)
  31415.927
  """
  return math.pi * radius ** 2

# =======================================================
# Exercise 2

LITRES_PER_GALLON = 4.54609
KMS_PER_MILE = 1.60934
def convert_to_litres_per_100_km(mpg: float) -> float:
    """
    Return the fuel effciency in Liters/Kilometer from Miles/Gallon
    Precondition: mpg > 0.
    >>>convert_to_litres_per_100_km(32)
    8.83
    >>>convert_to_litres_per_100_km(8)
    35.31
    >>>convert_to_litres_per_100_km(250)
    1.13
    """
    return (LITRES_PER_GALLON / (KMS_PER_MILE*mpg))*100

# =======================================================
# Exercise 3
def accumulated_amount(principal: float, rate: float, n: int, time: int) -> float:
    """
    Return a sum of money from principal + interest gained from an investment over a amount of time.
    Preconditions: principal > 0, rate > 0, time > 0, n > 0
    >>>accumulated_amount(1500,4.3,4,6)
    1938.84
    >>>accumulated_amount(2000,1,12,8)
    4347025.59
    >>>accumulated_amount(5250.99,6.9,6,2)
    51227446.71
    """
    return principal * (1 + (rate/n)) ** (n*time)

# =======================================================
# Exercise 4
def area_of_cone(height: float, radius: float) -> float:
    """
    Return the area of a cone from the radius and height of the cone
    Preconditions: radius > 0, height > 0
    >>>area_of_cone(1,1)
    4.44
    >>>area_of_cone(8,4)
    112.4
    >>>area_of_cone(12,16)
    753.98
    """
    return math.pi*height*(math.sqrt(radius**2 + height**2))
print (area_of_cone(8,4))

# =======================================================
# Exercise 5

def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    """
    Return the distance between two points, given by the coordinates (x1, y1) and (x2, y2).
    Precondition: x == int, y == int
    >>>distance(1,2,3,4)
    2.828
    >>>distance(80,67,32,24)
    64.44
    >>>distance(100,69,400,250)
    350.37
    """
    return math.sqrt((y2-y1)**2 + (x2-x1)**2)

def area_of_circle(xc: int, yc: int, xp: int, yp: int) -> float:
    """
    Return the area of a circle from 4 points in a 2d cartisian plane
    Precondition: x == int, y == int
    >>>area_of_circle(1,3,2,4)
    6.283
    >>>area_of_circle(14,12,45,21)
    3273.54
    >>>area_of_circle(4,125,58,57)
    23687.61
    """
    return math.pi * (math.sqrt((yp-yc)**2 + (xp-xc)**2))**2
