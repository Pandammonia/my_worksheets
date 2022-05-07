import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/ant_data.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header = next(reader)
	ice_thick, dates = [],[]
	for row in reader:
		meas = float(row[6])
		date = datetime.fromisoformat(row[4]) 
		dates.append(date)
		ice_thick.append(meas)




plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(ice_thick, dates, c='red')

#format plot
plt.title("AntArc", fontsize=24)
plt.xlabel('', fontsize = 16)
plt.ylabel("Ice", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()