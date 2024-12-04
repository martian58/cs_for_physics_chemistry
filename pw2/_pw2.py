import numpy as np
import matplotlib.pyplot as plt
import os

# Ensure the ./data directory exists
os.makedirs('./pw2/data', exist_ok=True)

# Set the random seed for reproducibility
np.random.seed(42)

# Define time range
t_start = 0
t_end = 20
dt = 0.01  # time step in seconds
t = np.arange(t_start, t_end + dt, dt)

# Question 1: Trajectory Generation
# 1.a. Compute position coordinates
x = 50 * np.sin(0.1 * np.pi * t)
y = 50 * np.sin(0.2 * np.pi * t)

# Plotting the trajectory
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Trajectory', color='blue')
plt.title('Car Trajectory from t=0 to t=20 seconds')
plt.xlabel('x(t) [meters]')
plt.ylabel('y(t) [meters]')
plt.legend()
plt.grid(True)
plt.axis('equal')  # Equal scaling for both axes
plt.savefig('./data/trajectory.png')
plt.close()  # Close the plot instead of showing it

# 1.b. Compute acceleration
# Given acceleration equations
a_x = -0.5 * np.pi**2 * np.sin(0.1 * np.pi * t)
a_y = -2 * np.pi**2 * np.sin(0.2 * np.pi * t)

# Plotting the acceleration
plt.figure(figsize=(8, 6))
plt.plot(t, a_x, label='Acceleration a_x(t)', color='red')
plt.plot(t, a_y, label='Acceleration a_y(t)', color='green')
plt.title('Acceleration Components over Time')
plt.xlabel('Time [seconds]')
plt.ylabel('Acceleration [m/s²]')
plt.legend()
plt.grid(True)
plt.savefig('./pw2/data/acceleration.png')
plt.close()

# Question 2: From Position to Acceleration
# 2.a. Adding Noise and Offset to Position Data
offset = 5  # Offset value
noise_std = 0.001  # Standard deviation (1 mm)
x_noisy = x + np.random.normal(loc=offset, scale=noise_std, size=x.shape)
y_noisy = y + np.random.normal(loc=offset, scale=noise_std, size=y.shape)

# 2.b. Calculating Acceleration from Noisy Position Data
dx_dt = np.gradient(x_noisy, dt)
dy_dt = np.gradient(y_noisy, dt)
a_x_noisy = np.gradient(dx_dt, dt)
a_y_noisy = np.gradient(dy_dt, dt)

# Plotting the noisy accelerations
plt.figure(figsize=(8, 6))
plt.plot(t, a_x_noisy, label='Noisy a_x(t)', color='purple')
plt.plot(t, a_y_noisy, label='Noisy a_y(t)', color='orange')
plt.title('Noisy Acceleration Components over Time')
plt.xlabel('Time [seconds]')
plt.ylabel('Acceleration [m/s²]')
plt.legend()
plt.grid(True)
plt.savefig('./pw2/data/noisy_acceleration.png')
plt.close()

# 2.c. Assessing the Impact of Noise and Offset
# Comparison of ideal vs noisy acceleration
plt.figure(figsize=(10, 8))
plt.subplot(2, 1, 1)
plt.plot(t, a_x, label='Ideal a_x(t)', color='red')
plt.plot(t, a_x_noisy, label='Noisy a_x(t)', color='purple', alpha=0.5)
plt.title('Comparison of Ideal and Noisy Acceleration a_x(t)')
plt.xlabel('Time [seconds]')
plt.ylabel('Acceleration [m/s²]')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t, a_y, label='Ideal a_y(t)', color='green')
plt.plot(t, a_y_noisy, label='Noisy a_y(t)', color='orange', alpha=0.5)
plt.title('Comparison of Ideal and Noisy Acceleration a_y(t)')
plt.xlabel('Time [seconds]')
plt.ylabel('Acceleration [m/s²]')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('./pw2/data/comparison_acceleration.png')
plt.close()

# Question 3: From Acceleration to Position
# 3.a. Adding Noise and Offset to Acceleration Data
accel_offset = 0.1  # Offset value
accel_noise_std = 1  # Standard deviation (1 m/s²)
a_x_noisy_2 = a_x + np.random.normal(loc=accel_offset, scale=accel_noise_std, size=a_x.shape)
a_y_noisy_2 = a_y + np.random.normal(loc=accel_offset, scale=accel_noise_std, size=a_y.shape)

# 3.b. Calculating Position from Noisy Acceleration Data
# Numerical integration using numpy.cumsum
x_position_noisy = np.cumsum(a_x_noisy_2) * dt
y_position_noisy = np.cumsum(a_y_noisy_2) * dt

# Plotting the noisy positions
plt.figure(figsize=(8, 6))
plt.plot(t, x_position_noisy, label='Noisy x(t)', color='cyan')
plt.plot(t, y_position_noisy, label='Noisy y(t)', color='magenta')
plt.title('Noisy Position Components over Time')
plt.xlabel('Time [seconds]')
plt.ylabel('Position [meters]')
plt.legend()
plt.grid(True)
plt.savefig('./data/noisy_position.png')
plt.close()

# 3.c. Assessing the Impact of Noise and Offset
# Comparison of ideal vs noisy position
plt.figure(figsize=(10, 8))
plt.subplot(2, 1, 1)
plt.plot(t, x, label='Ideal x(t)', color='blue')
plt.plot(t, x_position_noisy, label='Noisy x(t)', color='cyan', alpha=0.5)
plt.title('Comparison of Ideal and Noisy Position x(t)')
plt.xlabel('Time [seconds]')
plt.ylabel('Position [meters]')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t, y, label='Ideal y(t)', color='orange')
plt.plot(t, y_position_noisy, label='Noisy y(t)', color='magenta', alpha=0.5)
plt.title('Comparison of Ideal and Noisy Position y(t)')
plt.xlabel('Time [seconds]')
plt.ylabel('Position [meters]')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('./data/comparison_position.png')
plt.close()