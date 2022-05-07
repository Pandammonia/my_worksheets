dreamvac = {}

activepoll = True
while activepoll:
	name = input("What is your name? ")
	vac = input("What is your dream vacation? ")
	dreamvac[name] = vac
	cont = input("Would you like to continue? (yes/no) ")
	if cont == 'no':
		activepoll = False

print(f"Poll results are:")
for name, vac in dreamvac.items():
	print(f"{name.title()} would like to go to {vac.title()}")