import matplotlib.pyplot as plt
x_val = range(1, 1001)
y_val = [x**2 for x in x_val]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_val, y_val, c=y_val, cmap=plt.cm.Blues, s=10) #passing c here colours the line, RGB values work, this specific syntax gradients

ax.set_title("Square numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 16)
ax.set_ylabel("Square of value", fontsize = 16)

ax.axis([0, 1100, 0, 1100000])
ax.ticklabel_format(style='plain')
ax.tick_params(axis='both', which='major', labelsize=16) 
plt.savefig('squares_plot.png', bbox_inches='tight')  # to save the plot replace show with plt.savefig()