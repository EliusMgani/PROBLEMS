# create a python program to read a number n and print the Natural Numbers Summation pattern
lower_number = int(input("Enter the First Number: "))
upper_number = int(input("Enter the Last Number: "))
for j in range(lower_number, upper_number+1):
   a = []
   for i in range(lower_number, j+1):
      print(i, sep = " ", end = " ")
      if(i<j):
         print("+", sep = " ", end = " ")
      a.append(i)
   print("=", sum(a))