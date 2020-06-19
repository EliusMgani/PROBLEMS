# create a python program to search the number of times a particular number occurs in a list
n = int(input("Enter the number of elements: "))
a = []
for i in range(1,n):
   b = int(input("Enter Elements: "))
   a.append(b)
k = 0
num  = int(input("Enter the Number to be Searched: "))
for j in a:
   if(j==num):
      k = k+1
print("The Number of Times", num, "appeared is: ", k)