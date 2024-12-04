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

# Noise settings: mean of 5 meters and standard deviation of 1 mm (0.001 meters)
noise_mean = 5
noise_std = 0.001

# Add noise to the trajectory
x_noisy = x + np.random.normal(loc=noise_mean, scale=noise_std, size=x.shape)
y_noisy = y + np.random.normal(loc=noise_mean, scale=noise_std, size=y.shape)

# Calculate the ideal accelerations
a_x_ideal = -0.5 * np.pi**2 * np.sin(0.1 * np.pi * t)
a_y_ideal = -2 * np.pi**2 * np.sin(0.2 * np.pi * t)

# Numerical differentiation to find velocities
v_x_noisy = np.gradient(x_noisy, dt)
v_y_noisy = np.gradient(y_noisy, dt)

# Numerical differentiation to find accelerations
a_x_noisy = np.gradient(v_x_noisy, dt)
a_y_noisy = np.gradient(v_y_noisy, dt)

# Plot the ideal and noisy accelerations for comparison
plt.figure(figsize=(12, 8))

# Plot acceleration in x direction
plt.subplot(2, 1, 1)
plt.plot(t, a_x_ideal, label='Ideal $a_x(t)$', color='blue')
plt.plot(t, a_x_noisy, label='Noisy $a_x(t)$', color='red', linestyle='--')
plt.title('Comparison of Ideal and Noisy Acceleration in x Direction')
plt.xlabel('Time [s]')
plt.ylabel('Acceleration $a_x(t)$ [m/s²]')
plt.legend()
plt.grid(True)

# Plot acceleration in y direction
plt.subplot(2, 1, 2)
plt.plot(t, a_y_ideal, label='Ideal $a_y(t)$', color='blue')
plt.plot(t, a_y_noisy, label='Noisy $a_y(t)$', color='red', linestyle='--')
plt.title('Comparison of Ideal and Noisy Acceleration in y Direction')
plt.xlabel('Time [s]')
plt.ylabel('Acceleration $a_y(t)$ [m/s²]')
plt.legend()
plt.grid(True)

# Save and close the plot
plt.tight_layout()
plt.show()
plt.savefig('./data/acceleration_comparison.png', dpi=300)
plt.close()

print("Acceleration comparison plot saved as 'acceleration_comparison.png'.")
