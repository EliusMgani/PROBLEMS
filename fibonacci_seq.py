# create a python program to display the fibonacci sequence up to n-th term
terms = int(input("Enter Number of Terms: "))

# the first two terms
n1,n2 = 0,1
count = 0

# check if the number of terms is valid
if (terms<=0):
   print("Please Enter the Positive Number")
elif (terms==1):
   print("Fibonacci Sequence up to",terms,":")
   print(n1)
else:
   print("Fibonacci Sequence: ")
   while(count<terms):
      print(n1)
      nth = n1 + n2
      # update values
      n1 = n2
      n2 = nth
      count += 1
