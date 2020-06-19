# create a python program to print largest even and largest odd number in a list
n = int(input("Enter the Number of Elements to be in the List: "))
b = []
for i in range(0,n):
   a = int(input("Enter the Elements of the List: "))
   b.append(a)
c = []
d = []
for i in b:
   if(i%2==0):
      c.append(i)
   else:
      d.append(i)
c.sort()
d.sort()
count1 = 0
count2 = 0
for k in c:
   count1 = count1 + 1
for j in d:
   count2 = count2 + 1
print()
print(c)
print("The Largest Even Number is: ",c[count1-1])
print()
print(d)
print("The Largest Odd Number is: ",d[count2-1])

