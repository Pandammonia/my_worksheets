list = []
squares = []
for value in range(1,10):
	squares.append(value**3)
print(f"{squares} are the first 10 square numbers")

players = ["fabio", "shearer", "henry", "seaman"]
print(f"The first three players are:\n")
for player in players[:3]:
	print(player.title())

mycolours = ["red", "blue", "green"]
snickerscolours = mycolours[:]
print(f"My favourite colours are {mycolours}\n")
print(f"Snickers favourite colours are {snickerscolours}")

mycolours.append("yellow")
snickerscolours.append("luke")

print(f"My favourite colours are {mycolours}\n")
print(f"Snickers favourite colours are {snickerscolours}")

guns = ["uzi", "mp40", "smg", "winchester", "30-06"]
for gun in guns[0:2]:
	print(f"The first two guns are: {gun}")

print(f"Three items from the middle are {guns[1:4]}")
print(f"The last three guns in the list are {guns[2:5]}")

snickersguns = guns[:]
print(guns)
print(snickersguns)
snickersguns.append(".50MEOWOMETER")
snickersguns.append(".40catibre")
print(snickersguns)
print(guns)