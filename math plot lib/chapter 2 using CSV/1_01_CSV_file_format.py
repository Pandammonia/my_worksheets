import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f: 
	reader = csv.reader(f) #reader variable = file opened with csv reader
	header_row = next(reader) #header row is the next row in the file 
	

	highs = []
	for row in reader:
		high = int(row[5]) #we know the highs are in row 5 so we assign high to row 5 in the file
		highs.append(high) #we add each row 5 entry to the list highs

print(highs)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

#format plot
plt.title("Daily high temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize = 16)
plt.ylabel("Temperature (F):", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()