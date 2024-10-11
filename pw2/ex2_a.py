import numpy as np
import matplotlib.pyplot as plt

# Time settings
t_start = 0
t_end = 20
dt = 0.01
t = np.arange(t_start, t_end + dt, dt)

# Original trajectory
x = 50 * np.sin(0.1 * np.pi * t)
y = 50 * np.sin(0.2 * np.pi * t)

noise_mean = 5
noise_std = 0.001

x_noisy = x + np.random.normal(loc=noise_mean, scale=noise_std, size=x.shape)
y_noisy = y + np.random.normal(loc=noise_mean, scale=noise_std, size=y.shape)

plt.figure(figsize=(10, 6))

# original trajectory
plt.plot(x, y, label='Original Trajectory', color='blue')

# noisy trajectory
plt.plot(x_noisy, y_noisy, label='Noisy Trajectory', color='red', linestyle='dotted')

# Add labels and title
plt.title('Car Trajectory from t=0 to t=20 seconds (With Noise)')
plt.xlabel('x(t) [meters]')
plt.ylabel('y(t) [meters]')
plt.legend()
plt.grid(True)
plt.axis('equal')

# Save the plot as a PNG file
plt.savefig('./data/noisy_trajectory_plot.png', dpi=300)
plt.close()

print("Noisy trajectory plot saved as './data/noisy_trajectory_plot.png'.")
