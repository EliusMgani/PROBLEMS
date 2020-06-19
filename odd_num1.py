# Create a Python Program to print Odd Numbers Within a Given range.
lower_boundary = int(input("Enter the lower boundary of the range: "))
upper_boundary = int(input("Enter the upper boundary of the range: "))
for x in range(lower_boundary, upper_boundary):
   if (x%2!=0):
      print(x)
