import numpy as np
import matplotlib.pyplot as plt



t_start = 0      
t_end = 20       
dt = 0.01         
t = np.arange(t_start, t_end + dt, dt)  


x = 50 * np.sin(0.1 * np.pi * t)
y = 50 * np.sin(0.2 * np.pi * t)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Trajectory', color='blue')
plt.title('Car Trajectory from t=0 to t=20 seconds')
plt.xlabel('x(t) [meters]')
plt.ylabel('y(t) [meters]')
plt.legend()
plt.grid(True)
plt.axis('equal') 

plt.savefig('./data/trajectory_plot.png', dpi=300)
plt.close()  

print("Trajectory plot saved as 'data/trajectory_plot.png'.")