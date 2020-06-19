# create a python program to find the sum of sine series
import math
from math import pi
x = int(input("Enter the Value of x in degree: "))
n = int(input("Enter the Number of Terms: "))
def sin(x,n):
   sine = 0
   for i in range(n):
      sign = (-1)**i
      y = x*(pi/180)
      sine = sine + ((y**(2.0*i+1))/math.factorial(2*i+1))*sign
   return sine
print(round(sin(x,n),2))
