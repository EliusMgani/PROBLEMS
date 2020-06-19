# create a python program to check if a number is a strong number
num = int(input("Enter a Number: "))
sum = 0
temp = num
while(num):
   i = 1
   f = 1
   r = num % 10
   while(i<=r):
      f = f*i
      i = i+1
   sum = sum + f
   num = num//10
if(sum==temp):
   print("The Number is aStrong Number..!!")
else:
   print("The Number is not a Strong Number..!!")