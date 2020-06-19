# create a python program to calculate the length of a string without using a library function
string = input("Enter a String: ")
count = 0
for i in string:
   count = count + 1
print("The length of the String is: ", count)