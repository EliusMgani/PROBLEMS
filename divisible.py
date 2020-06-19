# create a python program to print all numbers in a range divisible by a given number
lowerNumber = int(input("Enter the lower number in a Range: "))
upperNumber = int(input("Enter the upper number in a Range: "))
n = int(input("Enter the number to be divisible: "))
for x in range(lowerNumber, upperNumber):
   if (n % x == 0):
      print(x)
print()