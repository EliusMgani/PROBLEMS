# create a python program to find the smallest divisor of an integer
n = int(input("Enter an integer: "))
a = []
for i in range(2, n+1):
   if (n%i==0):
      a.append(i)
a.sort()
print(a)
print()
print("smallest divisor: ", a[0])
print()