import matplotlib.pyplot as plt 	

x_val = range(1,5001)
y_val = [y**3 for y in x_val]


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_val, y_val, c='red', s=10)
ax.set_title("Cubes", fontsize =24)
ax.set_xlabel("Value", fontsize=18)
ax.set_ylabel("Cube of value", fontsize=18)

ax.axis([0, 1100, 0, 11000000000])
ax.ticklabel_format(style='plain')
ax.tick_params(axis='both', which='major', labelsize=16) 
plt.show()