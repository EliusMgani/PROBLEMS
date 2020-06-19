# create a python program to find the sum of the series: 1+(x^2)/2+(x^3)/3+....+(x^n)/n
n = int(input("Enter the number of Terms: "))
r = int(input("Enter the Value of x: "))
sum1 = 1
for i in range(2, n+1):
   sum1 = sum1 + ((r**i)/i)
print("The Sum of of the Series is: ", round(sum1, 2))