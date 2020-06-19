# create a python program to reverse a given list of numbers
list_of_numbers = []
num = int(input("How Many Numbers are You going to Enter : "))
for x in range(num):
   Elements = int(input("Enter the Numbers of a List : "))
   list_of_numbers.append(Elements)
print()
print("Numbers of a List are: ")
print(list_of_numbers)
print()
print("The Reversed Numbers of a List are:")
print(list_of_numbers[ : :-1])
print()