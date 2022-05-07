cars = ["audi", "subaru", "merc", "bmw"]
print(cars)
print(sorted(cars)) # temperary sorter
print(cars)
cars.reverse() #reverses list
print(cars)

#store 5 places in a list at random

topvisit = ["Chernobyl", "Ukraine", "Gobekli tepe", "Uintah", "Pripyat"]
print(topvisit)
print(sorted(topvisit))
print(topvisit)
print(sorted(topvisit, reverse=True))
print(topvisit)
topvisit.reverse()
print(topvisit)
topvisit.reverse()
print(topvisit)
topvisit.sort()
print(topvisit)
topvisit.sort(reverse=True)
print(topvisit)

dinner = ["Snickers", "Luke", "Clare"]
numberofinvites = f"I will be inviting {len(dinner)} people to dinner tomorrow!"
print(numberofinvites)

shooters = ["m1911", "remmington", ".45", "desert eagle"]
print(shooters)
print(sorted(shooters))
print(shooters)
shooters.sort()
print(shooters)
weapon = f"My {shooters[0:4]} is a deadly weapon"
print(weapon)

print(shooters)
shooters.append("sawn off")
print(shooters)
shooters.insert(1, "Pump action")
print(shooters)
shooters.sort()
removedweapon = shooters.pop()
removal = f"I have removed {removedweapon} from the list."
print(removal)
print(shooters)
secondremovedweapon = shooters.pop()
secondr = f"I have also removed {secondremovedweapon} from the list. It is now a list of {len(shooters)} weapons"
print(secondr)