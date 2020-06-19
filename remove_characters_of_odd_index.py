# create a python program to remove the characters of odd index values in a string
string = input("Enter a String: ")
def modify(string):
   Final = ""
   for i in range(len(string)):
      if(i % 2 == 0):
         Final = Final + string[i]
      return Final
print("The Modified String is:")
print(modify(string))