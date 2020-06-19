# create a python program to check if a number is a perfect number
n = int(input("Enter any Number: "))
sum = 0
for x in range(1,n):
   if(n % x == 0):
      sum = sum + x
if(sum == n):
   print("The Number is a Perfect Number..!!")
else: 
   print("The Number is not a Perfect Number..!!")