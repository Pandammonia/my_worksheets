alien_0 = {'colour':'green', 'points':'5',}
alien_1 = {'colour':'yellow','points':'10',}
alien_2 = {'colour':'red', 'points':'15',}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

#empty alien list
alienfleet = [] #make an empty list to store all these aliens
for alien_number in range(30): #run the loop 30 times
	new_alien = {'colour':'green', 'points': '5', 'speed':'slow',} #new alien characteristics
	alienfleet.append(new_alien) #append new alien to the fleet


for new_alien in alienfleet[:3]:
	if new_alien['colour'] == 'green':
		new_alien['colour'] = 'yellow'
		new_alien['speed'] = 'medium'
		new_alien['points'] = '10'

#show first five aliens
for aliens in alienfleet[:5]:
	print(aliens)
print(f"Total number of aliens: {len(alienfleet)}")

