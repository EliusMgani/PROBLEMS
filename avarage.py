# create a python program to calculate the average of numbers in a given list
list_first = []
num = int(input("How Many Numbers : "))
for x in range(num):
   numbers = int(input("Enter Numbers : "))
   list_first.append(numbers)
sum = sum(list_first)
print("The sum of Elements in a Given List is ", sum)
print()
average = sum/2
print("The Average of Elements in a Given List is ", average)
print()