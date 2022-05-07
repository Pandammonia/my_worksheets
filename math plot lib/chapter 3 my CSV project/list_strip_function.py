import csv
import matplotlib.pyplot as plt

def liststripper(oldlist):
	no = -9999.0
	newlist = []
	newlist = [x for x in oldlist if x != no]
	return newlist


filename = 'data/ant_data.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	print(header_row)
	ice_thick = []
	for row in reader:
		ice_thickn = float(row[6])
		ice_thick.append(ice_thickn)
		
ice_thick_stripped = liststripper(ice_thick)


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot (ice_thick_stripped)
#format plot
plt.title("Antarctica Ice Thickness", fontsize=24)
plt.xlabel('', fontsize = 16)
plt.ylabel("Ice Thickness (m)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
ax.set_xticks([], [])
plt.show()