# create a python program to find the gravitational force acting between two objects
m1 = float(input("Enter the First Mass: "))
m2 = float(input("Enter the Second Mass: "))
r = float(input("Enter the Distance Between the Centers of the Masses: "))
G = 6.673*(10**-11)
F = (G*m1*m2)/(r**2)
print("Hence, The Gravitational Force is: ", round(F,2), "N")
print()