# create a python program to check if a number is an Armstrong Number
n = int(input("Enter Any Number: "))
a = list(map(int,str(n)))
b = list(map(lambda x:x**3,a))
print(a)
print()
print(b)
if(sum(b)==n):
   print("The Number is ArmStrong Number..!!")
else:
   print("The Number is not ArmStrong Number..!!")