import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
L = 1.0  # Length of the pendulum (m)
g = 9.81  # Acceleration due to gravity (m/s^2)

# Define the system of equations
def double_pendulum(t, y):
    theta1, omega1, theta2, omega2 = y
    c = np.sin(theta1 - theta2)
    s = np.cos(theta1 - theta2)
    
    K = L**2 - c**2
    
    dtheta1_dt = omega1
    dtheta2_dt = omega2
    domega1_dt = (1 / K) * (g * np.sin(theta2) * c - 2 * np.sin(theta1) + L * s * omega1**2 * c + omega2**2)
    domega2_dt = (1 / K) * (2 * g * np.sin(theta1) * c - np.sin(theta2) - L * s * omega2**2 * c + 2 * omega1**2)
    
    return [dtheta1_dt, domega1_dt, dtheta2_dt, domega2_dt]

# Time span for the simulation
t_span = (0, 10)  # 10 seconds
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # 1000 time points for evaluation

# Initial conditions for (theta1 = 45°, theta2 = -45°)
theta1_1 = np.radians(45)  # Convert to radians
theta2_1 = np.radians(-45)
initial_conditions_1 = [theta1_1, 0, theta2_1, 0]  # [theta1, omega1, theta2, omega2]
solution_1 = solve_ivp(double_pendulum, t_span, initial_conditions_1, t_eval=t_eval)

# Initial conditions for (theta1 = 30°, theta2 = 0°)
theta1_2 = np.radians(30)
theta2_2 = 0
initial_conditions_2 = [theta1_2, 0, theta2_2, 0]
solution_2 = solve_ivp(double_pendulum, t_span, initial_conditions_2, t_eval=t_eval)

# Calculate positions of the second mass (x2, y2)
x2_1 = L * (np.sin(solution_1.y[0]) + np.sin(solution_1.y[2]))
y2_1 = -L * (np.cos(solution_1.y[0]) + np.cos(solution_1.y[2]))

x2_2 = L * (np.sin(solution_2.y[0]) + np.sin(solution_2.y[2]))
y2_2 = -L * (np.cos(solution_2.y[0]) + np.cos(solution_2.y[2]))

# Plotting the trajectories
plt.figure(figsize=(12, 6))

# Trajectory for (theta1 = 45°, theta2 = -45°)
plt.subplot(1, 2, 1)
plt.plot(x2_1, y2_1, label='Trajectory (θ1=45°, θ2=-45°)', color='blue')
plt.title('Trajectory of Second Mass (θ1=45°, θ2=-45°)')
plt.xlabel('x2 (m)')
plt.ylabel('y2 (m)')
plt.axhline(0, color='grey', lw=0.5, ls='--')
plt.axvline(0, color='grey', lw=0.5, ls='--')
plt.grid()
plt.axis('equal')

# Trajectory for (theta1 = 30°, theta2 = 0°)
plt.subplot(1, 2, 2)
plt.plot(x2_2, y2_2, label='Trajectory (θ1=30°, θ2=0°)', color='orange')
plt.title('Trajectory of Second Mass (θ1=30°, θ2=0°)')
plt.xlabel('x2 (m)')
plt.ylabel('y2 (m)')
plt.axhline(0, color='grey', lw=0.5, ls='--')
plt.axvline(0, color='grey', lw=0.5, ls='--')
plt.grid()
plt.axis('equal')

plt.tight_layout()
plt.savefig('./pw3/data/3_a.png')

