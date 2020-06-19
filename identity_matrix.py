# create a python program to print an identity matrix
n = int(input("Enter a Number: ")) 
for x in range(0, n): 
   for y in range(0, n):
      if(x==y):
         print(1, sep = " ", end = " ")
      else:
         print(0, sep = " ", end = " ")
   print()