# create a python program to read a number n and print the series 1+2+3+...+n=
lower_number = int(input("Enter the first number: "))
upper_number = int(input("Enter the last number: "))
a = []
for i in range(lower_number, upper_number):
   print(i, sep = " ", end = " ")
   if(i<upper_number):
      print("+", sep = " ", end = " ")
   a.append(i)
print("=", sum(a))