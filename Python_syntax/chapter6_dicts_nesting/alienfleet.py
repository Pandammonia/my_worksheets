alienfleet =[]
#make 30 green aliens
for alien_number in range(30):
	new_alien = {'colour':'green', 'points': '5', 'speed':'slow',}
	alienfleet.append(new_alien)
for new_alien in alienfleet[:3]:
	if new_alien['colour'] == 'green':
		new_alien['colour'] = 'yellow'
		new_alien['speed'] == 'medium'
		new_alien['points'] == '10'
#show first five aliens
for aliens in alienfleet[:5]:
	print(aliens)