import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.tick_params(colors='white')  # Set tick color to white
x = np.linspace(0, 6 * np.pi, 3000)

sin_line, = ax.plot(x, np.sin(x), color='purple', linewidth=3)
cos_line, = ax.plot(x, np.cos(x), color='cyan', linewidth=3)
ax.set_ylim(-5, 5)
ax.set_xlim(0, 6 * np.pi)  
ax.set_yticks(np.arange(-5,6,1))  # Set y-axis ticks
ax.set_xticks(np.arange(0, 6*np.pi + np.pi/2, np.pi/2)) # Set x-axis ticks
ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π', '5π/2', '3π', '7π/2', '4π', '9π/2', '5π', '11π/2', '6π', '13π/2'], color='white')  # Set x-axis tick labels and color
def update(frame):
    sin_line.set_ydata(1*np.sin(x + frame/10)) 
    cos_line.set_ydata(1*np.cos(x + frame/10))
    return sin_line, cos_line
ani = FuncAnimation(fig, update, frames=10000, interval=20)
ax.set_title('Animated Sine and Cosine Waves', color='purple')  # Set title and color
plt.show()
