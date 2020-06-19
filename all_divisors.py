# create a python program to generate all the divisors of an integer
n = int(input("Enter an Integer: "))
print("The Divisors of an Integer are: ")
for i in range(1, n+1):
   if(n % i == 0):
      print(i)