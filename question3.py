# Authors: Samwel, Josephine, Modester
# GitHub handles: @Sammyiel, @Josephine-uwizeye, @Modester-mw

# Define the following functions using your dynamic array class as an input. Use only
# the methods that you have defined (len, get, set, add, del) - not built-in methods.
# a. contains(array, val) which returns True if val is in the array
# b. reverse(array) which reverses the entire array (outputting a new array)
# c. insert(array, val, i) which inserts a value at the given index

# importing modules
from numpy import random

array1 = []
i = 0
while i < 5:
   i += 1
   x = random.randint(10) + 1
   array1.append(x)


class Array:

   def check_val(self, val):
       print(array1)
       for j in array1:
           if j == val:
               return True
       return False

   def reverse(self):
       val2 = int(input("Enter number to be reversed: "))
       rev_num = 0
       while val2 > 0:
           rem = val2 % 10
           rev_num = (rev_num * 10) + rem
           val2 //= 10
       print(f"This is the reversed number: {rev_num}\n\n")

   def insert(self, val, i):
       x = 0
       for _ in array1:
           x += 1
           if x == i:
               array1[x] = val
       print(f"{array1}\n\n")


ans = 0
while ans < 3:
   ans += 1
   action = int(
       input("Choose action:(1, 2 or 3)\n1 Check if value is available\n2 Reverse number\n"
             "3 Insert value in an array\n>>> "))

   if action == 1:
       val1 = int(input("Enter value between 1 and 10 to search: "))
       print(f"{Array.check_val(array1, val1)}\n\n")

   elif action == 2:
       Array.reverse("Self")

   elif action == 3:
       i = int(input("Enter position/index to insert value: "))
       val = int(input("Enter value to insert: "))
       Array.insert(array1, val, i)




