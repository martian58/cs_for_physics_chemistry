import numpy as np
import matplotlib.pyplot as plt

t_start = 0      
t_end = 20        
dt = 0.01         
t = np.arange(t_start, t_end + dt, dt) 


# Equations
a_x = -0.5 * (np.pi ** 2) * np.sin(0.1 * np.pi * t)
a_y = -2 * (np.pi ** 2) * np.sin(0.2 * np.pi * t)

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, a_x, label='Acceleration a_x(t)', color='red')
plt.title('Acceleration Components over Time')
plt.xlabel('Time [seconds]')
plt.ylabel('a_x(t) [m/s²]')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t, a_y, label='Acceleration a_y(t)', color='green')
plt.xlabel('Time [seconds]')
plt.ylabel('a_y(t) [m/s²]')
plt.legend()
plt.grid(True)

# Adjust layout and save the acceleration plot
plt.tight_layout()
plt.savefig('./data/acceleration_plot.png', dpi=300)
plt.close() 

print("Acceleration plot saved as 'data/acceleration_plot.png'.")