#CREATING ARRAYS USING ARRAY MODULE 
#--1D arrays only
#--built in module (no need to install)
#--simple,slow, memory-efficient storage
#--homogeneous arrays can be made (same datatype arrays)


# import array as arr   #arr is an alias name
from array import * #import all (now no need to write arr before every function call of array module)


# arr1 = arr.array('i',[1,2,3,4,5,6]);    #i here tells the type of array we want to create (i represemt 2 byte int array) and this is called TYPE CODE

arr1 = array('i',[1,2,3,4,5,6]); #using import all ..no need to write arr. 
#type code i for int, d for decimal(float), u for unicode(characters)

for u in range(0,6):
    print(arr1[u], end=", ")  #end="," is called delimeter        

print()
#iterating using enhanced for loop
for z in arr1:
    print(z,end=" | ")

print()

print("length of array:",len(arr1))
print("type code of array:",arr1.typecode)

#reversing an array
print("reversed array: ",end="")
arr1.reverse()      #mutable
for z in arr1:
    print(z,end=" | ")

print()

#updating an array by inserting an element
print("updated array: ",end="")
arr1.insert(3,100)  #index, val
arr1.append(200) #insert at the end of array
arr1[0] = 300   #replacing an element (overwriting)
for z in arr1:
    print(z,end=" | ")
print()

print("copy of arr1: ",end="")
copyArr1 =array(arr1.typecode,arr1)
for z in copyArr1:
    print(z,end=" | ")
print()

#removing element from array 
print("after deleting elements: ",end="")
copyArr1.pop(0) #takes index as arg .....if not index is provided , will pop out the last element 
copyArr1.remove(200) #takes element as arg 
for z in copyArr1:
    print(z,end=" | ")
print()

#array slicing
print("Sliced Array: ",end="")
# slicedArr = arr1[startIndex:stopIndex]
slicedArr = arr1[2:5]
for z in slicedArr:
    print(z,end=" | ")
print()

print("reversing array using slicing: ",end="")
reverseSlicedArr = arr1[::-1]
for z in reverseSlicedArr:
    print(z,end=" | ")
print()

# dynamically taking element as input for array during run time
# arr2 = array("i",[ ])
# n = int(input("Enter size of array: "))
# for i in range(0,n):
#     arr2.append(int(input(f"enter element number {i+1}: ")))
# print()

arr2= array("i",[11,22,33,44,55,66,77])
# for z in arr2:
#     print(z,end=" | ")
# print()

print("index of 44 is: ",arr2.index(44)) #takes element as arg... #returns the index of element