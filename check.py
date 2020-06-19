# write a function in python which detects whether the given two strings are anagrams or not
def check(a,b):
   if (len(a) != len(b)):
      return False
   elif (sorted(list(a)) == sorted(list(b))):
      return True
   else:
      return False