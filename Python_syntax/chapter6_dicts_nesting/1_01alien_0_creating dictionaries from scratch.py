alien_0 = {'colour': 'green', 'points' : 5}
print(alien_0['colour'])
print(alien_0['points'])

newpoints = alien_0['points']
print(f"You just earned {newpoints} points!")

alien_0['x position'] = 0 # add new keys to dictionary
alien_0['y position'] = 25
print(alien_0) # shhows theyre added 

alien_0 = {} # this starts alien_0 from scratch 
alien_0['colour'] = 'green' # adds the colour green
alien_0['points'] = 5 # adds the points value 5
print(alien_0)

alien_0['colour'] = 'yellow'
print(f"The alien colour is {alien_0['colour']}")

#move my alien right
#determine how far to move it based on its speed

alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
alien_0['points'] = 5

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment #new position is old position + the increment

print(f"New alien position is {alien_0['x_position']}")

print(alien_0)

del alien_0['points']
print(alien_0)
