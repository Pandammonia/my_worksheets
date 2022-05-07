simple_array = [[2,5,8],[3,5,5],[1,6,9]]  #3x3 grid, 2,5,8 iss top row, 3,5,5 is second
print(simple_array)
print(simple_array[1])
simple_array[1][1] = 6 #change [row1][column1] to 6
print(simple_array)
#labelled 2d dictionary
labelled_dict = {"A":{"x":54, "y":22, "z":11}, "B":{"x":29, "y": 43, "z": 81}}
print(labelled_dict)
for i in labelled_dict:
	print(labelled_dict [i]["y"])

