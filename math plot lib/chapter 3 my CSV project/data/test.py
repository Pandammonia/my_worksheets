import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/ant_data.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header = next(reader)