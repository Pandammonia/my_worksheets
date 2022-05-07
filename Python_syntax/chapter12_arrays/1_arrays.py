import array

"""How to create, update, index, pop, delete print out etc, Arrays"""

#creating array with integer type
x = array.array('i',[1,2,3])
print("The new array is: ", end="")
for i in range(0,3):
	print(x[i], end = " ")
print()

#creating an array with floats
y = array.array('d', [4.5, 5.5, 6.5])
#print original array
print("The new created array is : ", end=" ")
for i in range(0,3):
	print(y[i], end=" ")
print()

#inserting into array "x" using .insert()

x.insert(2,3) #insert at index 2 integer 3  
print("Array after insertion :", end= " ")
for i in (x):
	print(i, end=" ")
print()

#adding into y using .append()
y.append(4.5) # adds 4.5 to end of array
print("Array after insertion: ", end="")
for i in (y):
	print (i, end=" ")
print()


#initilize array
arr = array.array('i', [2,4,6,2,8])
print(arr)
#using pop() to remove component at 2nd position
print("The popped element is: ", end="")
print(arr.pop(2)) #prints 6

print("The array after popping is : ", end="")
for i in range (0,4): 
	print(arr[i], end=" ")
print("\r")

#use remove() to remove 1st occurence of 2
arr.remove(2)
print("The array after removing will be: ", end="")
for i in range(0,3):
	print(arr[i], end="")
print("\r")

#initlize an arr
arr = array.array('i', [4,5,6,4,5,8])
#print original array
print("The new array is :", end="")
for i in range(0,6):
	print(arr[i], end="")
print("\r")

#use index() to print index of 5
print("The index of 5 is: ", end="")
print(arr.index(5))
#use index to print index of 8
print("The index of 8 is: ", end ="")
print(f"{arr.index(8)}\n")

arr=array.array('i', [5,6,7,5,6,8])
#printing pre-defined array
print("Array before any updation: ", end="")
for i in range(0,6):
	print(arr[i], end=" ")
print() 
#update an element in the array
arr[5] = 9
print("Array after update: ", end="")
for i in range(0,6):
	print(arr[i], end=" ")
print()

arr[2] = 10
print("Array after second update: ",end="")
for i in range(0,6):
	print(arr[i], end=" ")
print()