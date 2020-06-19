# create a python program to find the sum of cosine series
import math
from math import pi
x = int(input("Enter the Value of x in Degree: "))
n = int(input("Enter the Number of Terms: "))
def cosine(x,n):
   cosx = 1
   sign = -1
   for i in range(2, n, 2):
      y = x*(pi/180)
      cosx = cosx + (sign*(y**i))/math.factorial(i)
      sign = -sign
   return cosx
print(round(cosine(x,n),2))