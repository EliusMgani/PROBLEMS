# create a python program to find the sum of first N natural number 
n = int(input("Enter a Number: "))
sum1 = 0
while(n>0):
   sum1 = sum1 + n
   n = n-1
print("The Sum of the First N Natural Number is: ", sum1)