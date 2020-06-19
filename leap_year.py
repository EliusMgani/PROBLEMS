# create a python program to check whether a given year is a leap year
year = int(input("Enter a Year to be Checked: "))
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
   print("The Year is a Leap")
else:
   print("The Year is not a Leap")