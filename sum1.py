# write a function to give the sum of all the numbers in a list
first = []
num = int(input("How Many Numbers : "))
for n in range(num):
   numbers = int(input("Enter Numbers : "))
   first.append(numbers)
print("Sum of Elements in a given List is : ", sum(first))
print()