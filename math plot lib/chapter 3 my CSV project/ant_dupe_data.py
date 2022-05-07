import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/ant_data.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header = next(reader)
	ice_thick, dates, long_ = [],[],[]
	for row in reader:
		meas = float(row[6])
		longs = float(row[2])
		date = datetime.strptime(row[4], '  %Y-%m-%d %H:%M:%S.%f')
		dates.append(date)
		ice_thick.append(meas)
		long_.append(longs)




plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(long_, ice_thick, c='blue', s=10)
plt.fill_between(long_, ice_thick, facecolor='blue', alpha = 0.1) 
#format plot
plt.title("Ice thickness of Thwaites Glacier in Antarctica", fontsize=24)
plt.xlabel('Longitude: (deg)', fontsize = 16)
plt.ylabel("Ice thickness (m)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()