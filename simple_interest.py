# create a python program to compute Simple Interest given all the required values
principle = int(input("Enter the principle amount: "))
rate = int(input("Enter the rate: "))
time = int(input("Enter the time in years: "))
simple_interest = (principle*rate*time)/100
print("The Simple Interest is : ", simple_interest)
