# create a python program to check ifa number is a Palindrome
n = int(input("Enter the Number: "))
temp = n
rev = 0
while(n>0):
   dig = n%10
   rev = rev*10+dig
   n = n//10
if(temp==rev):
   print("The Number is a Palindrome")
else:
   print("The Number is not Palindrome")
