import random
import matplotlib.pyplot as plt 
x = 0
y = 0
x_points = []
y_points = []
iterations = 100000    
for _ in range(iterations):
    r = random.random()
    if r < 0.01:
        x_new = 0
        y_new = 0.16 * y
    elif r < 0.86:
        x_new = 0.85 * x + 0.04 * y
        y_new = -0.04 * x + 0.85 * y + 1.6
    elif r < 0.93:
        x_new = 0.2 * x - 0.26 * y
        y_new = 0.23 * x + 0.22 * y + 1.6
    else:
        x_new = -0.15 * x + 0.28 * y
        y_new = 0.26 * x + 0.24 * y + 0.44
    x, y = x_new, y_new
    x_points.append(x)
    y_points.append(y)
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.scatter(x_points, y_points, s=0.1, color='forestgreen')
ax.axis('off')
ax.set_title("Barnsley Fern", color='white', fontsize=16)

plt.show()  
