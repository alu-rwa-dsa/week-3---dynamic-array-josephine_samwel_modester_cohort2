#Authors:Modester, Samwel, Josephine

#Question:Create a dynamic array subclass which also has the following basic methods:

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


