# create the python program to Swap Numbers without using a temporary variable
a = int(input("Enter the Values of First Variable : "))
b = int(input("Enter the Values of Second Variable : "))
a = a + b
b = a - b
a = a - b
print("a is : ", a, "b is : ", b)
print()