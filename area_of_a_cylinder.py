# create a python program to find surface area of a cylinder
from math import pi
h = float(input("h: "))
r = float(input("r: "))
# area of a circle
circles = 2*pi*r**2

# area of a side
side = 2*pi*r*h

# surface area of a cylinder
area = circles + side

print(area)