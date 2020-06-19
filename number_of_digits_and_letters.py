# create a python program to calculate the number of digits and letters in a string
string = input("Enter the String: ")
count1 = 0
count2 = 0
for i in string:
   if(i.isdigit()):
      count1 = count1 + 1
   elif(i.isalpha()):
      count2 = count2 + 1

print("The Number of Digits are: ")
print(count1)
print("The Number of Letters are: ")
print(count2)