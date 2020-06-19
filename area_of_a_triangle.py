# create a python program to find the area of a triangle given all three sides
import math
a = int(input("Enter The first Side: "))
b = int(input("Enter The Second Side: "))
c = int(input("Enter The Third Side: "))
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The Area of a Triangle is: ", round(area,2))
print()


# alternatively:
base = float(input("Enter the Base of a Triangle: "))
height = float(input("Enter the Height of a Triangle: "))
ares_of_a_triangle = 0.5*base*height
print(ares_of_a_triangle)