# create a python program to read height in centimeters and then convert the height to feet and inches
centimeter = int(input("Enter the Height in centimenters: "))
inches = 0.394*centimeter
feet = 0.0328*centimeter
print("The height in Inches is: ", round(inches,3))
print("The height in feet is: ",round(feet,3))
