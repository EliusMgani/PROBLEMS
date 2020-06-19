# create a python program to detect if two string are anagrams numbers
s1 = input("Enter the First String: ")
s2 = input("Enter the Second String: ")
if(sorted(s1)==sorted(s2)):
   print("The two String are Anagrams..!!")
else:
   print("The Two String are Not Annagram..!!")