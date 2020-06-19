# create a python program to find the sum of digits in a number
r = int(input("Enter a Number: "))
tot = 0
while(r>0):
   dig = r%10
   tot = tot + dig
   r = r//10
print("The Sum Of the Digits is: ", tot)
print()