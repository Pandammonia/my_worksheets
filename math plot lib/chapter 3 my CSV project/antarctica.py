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
		

print(ice_thick)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(ice_thick)
plt.title('Ice thickness in Antarctica', fontsize = 24)
plt.xlabel('')
plt.ylabel('Ice thickness (m)', fontsize = 18)
plt.tick_params(axis='both', labelsize=10)
plt.show()