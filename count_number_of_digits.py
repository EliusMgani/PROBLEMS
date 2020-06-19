# create a python program to count the number of digits in a number
s = int(input("Enter the number: "))
count = 0
while(s>0):
   count = count + 1
   s = s//10
print("The number of digits of a given number: ", count)
print()