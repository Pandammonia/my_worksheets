import csv
import matplotlib.pyplot as plt

filename = 'data/ant_data.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	print(header_row)
	ice_thick = []
	for row in reader:
		ice_thickn = float(row[6])
		ice_thick.append(ice_thickn)
		remove = -9999.0 #string to remove
		ice_thick_new = [x for x in ice_thick if x != remove]
		return ice_thick_new

print(ice_thick_new)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(ice_thick_new)
plt.title('Ice thickness in Antarctica', fontsize = 24)
plt.xlabel('')
plt.ylabel('Ice thickness (m)', fontsize = 18)
plt.tick_params(axis='both', labelsize=10)
plt.show()