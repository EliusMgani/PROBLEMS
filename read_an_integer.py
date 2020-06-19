# create a python program to read an integer. for all non integers i<N, print i**2
n = int(input("Enter Any Integer: "))
print(*[num**2 for num in range(n)], sep = "\n")
