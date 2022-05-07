import array as arr

arr2 = arr.array('i', [4,5,6,4,5,8])
#print original array
print("The new array is :", end="")
for c in range(0,6):
	print(arr2[c], end="")
print("")