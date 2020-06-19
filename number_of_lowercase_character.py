# create a python program to count number of lowercase characters in a string
string = input("Enter a String: ")
count = 0
for i in string:
   if(i.islower()):
      count = count + 1
print("The Number of Lowercase Character is: ")
print(count)