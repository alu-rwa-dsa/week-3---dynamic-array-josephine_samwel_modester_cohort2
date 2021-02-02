#Authors:Modester, Samwel, Josephine

#Question:simple array class  where each element must be an integer type and:
#has a .len() method which outputs the length of the array
from array import *

weights_Array=[] #representing an array in list
class weights():
    def __int__(self,height):
        self.height = height
weights_Array.append(50)
weights_Array.append(35)
weights_Array.append(45)
print(weights_Array)


print(weights_Array.__len__())#this inbuilt method prints the size of array

print(weights_Array.__getitem__(1))

weights_Array.__setitem__(0,55)
print(weights_Array)






