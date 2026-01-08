#CREATING ARRAYS USING PYTHON NUMPY MODULE 
#--multi Dimensional array
#--pip intall numpy
#--very fast and efficient 
#--heterogeneous arrays can be made (multiple diff datatypes in same array)


import numpy as np # type: ignore
# from numpy import * 



arr1 = np.array([1,2,3,4,5,6,7]) 
print("Array: ",end="")
for c in arr1:
    print(c,end=", ")
print()

#creatnig array using AP
 
#linspace(start:stop:No of partitions)
print("Array using Linspace: ",end="")
arr2 = np.linspace(10,100,10)
for c in arr2:
    print(c,end=", ")
print()

#arange(start:stop:step)
print("Array using arange: ",end="")
arr3 = np.arange(10,21,2)
for c in arr3:
    print(c,end=", ")
print()

#logspace(start:stop:step) ...will create an array in form of log (e^)
print("Array using logspace: ",end="")
arr4 = np.logspace(10,21,2)
for c in arr4:
    print(c,end=", ")
print()

#zeros(size) ...will create an array full of Zero 0
print("Array using zeros: ",end="")
arr5 = np.zeros(5)
for c in arr5:
    print(c,end=", ")
print()

#ones(size) ...will create an array full of One 1
print("Array using ones: ",end="")
arr6 = np.ones(5)
for c in arr6:
    print(c,end=", ")
print()

#full(size,element) ...will create an array full of the element provided
print("Array using full: ",end="")
arr7 = np.full(6,7)
for c in arr7:
    print(c,end=", ")
print()


#Dimensional arraysssss
print("DIMENSIONAL ARRAYS: ")

print("zero: ",end="")
zero = np.array(10) #single element array
print(zero)

print("one:",end="")
one = np.array([1,2,3,4,5]) #1D array
print(one)

#in multidimensional arrays the size of inner arrays should be equally distributed 
#eg, [[1,1,1],[2,2],[3,3,3,3]] is wrong ,,, [[1,1,1],[2,2,2],[3,3,3]] is correct
print("two: ")
two = np.array([[1,2,3],[3,4,5],[5,6,7]]) #2D array (collection of 1D arrays)
print(two)

print("three: ")
three= np.array([[[1,1,1],[2,2,2],[3,3,3]],[[4,4,4],[5,5,5],[6,6,6]],[[7,7,7],[8,8,8],[9,9,9]]]) #3D array (collection of 2D arrays)
print(three)
