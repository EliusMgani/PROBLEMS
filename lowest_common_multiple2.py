# create a python program to find the LCM of three numbers
a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))
c = int(input("Enter the Third NUmber: "))
if(a>b):
   min1=a
elif(b>c):
   min1=b
else:
   min1=c
   while(1):
      if(min1%a==0 and min1%b==0 and min1%c==0):
         print("The LCM is: ",min1)
         break
      min1 = min1 + 1