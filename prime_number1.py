# create a python program to check if a number is a prime number
a = int(input("Enter a Number: "))
k = 0
for i in range(2, a//2+1):
   if(a%i==0):
      k = k+1
if(k<=0):
   print("The Number is a Prime Number..!!")
else:
   print("The Number is Not Prime Number..!!")