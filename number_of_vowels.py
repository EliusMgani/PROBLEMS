# create a python program to count the number of vowels in a string
string = input("Enter the String: ")
vowels = 0
for i in string:
   if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' 
      or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'
      ):
      vowels = vowels + 1
print("The Number of Vowels in a String is")
print(vowels)