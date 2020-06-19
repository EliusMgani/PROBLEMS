# create a python program to find the LCM of two numbers
a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))
if(a>b):
   min1=a
else:
   min1=b
while(1):
   if(min1%a==0 and min1%b==0):
      print("LCM is: ",min1)
      break
   min1 = min1 + 1