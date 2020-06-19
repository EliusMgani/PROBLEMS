# create a python program to remove the nth index character from a non empty string
string = input("Enter the String: ")
n = int(input("Enter the index of a Character to be Removed: "))
def remove(string, n):
   first = string[ :n]
   last = string[n+1: ]
   return first + last
print("Modified String is: ")
print(remove(string,n))