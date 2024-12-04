import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)
L = 0.2   # Length of the pendulum (m) -> 20 cm
theta0 = np.radians(15)  # Initial angle (radians) for small angle case
theta0_large = np.radians(75)  # Initial angle for large angle case

# Define the system of equations
def pendulum(t, y):
    theta1, theta2 = y
    dtheta1_dt = theta2
    dtheta2_dt = - (g / L) * np.sin(theta1)
    return [dtheta1_dt, dtheta2_dt]

# Time span for the simulation
t_span = (0, 10)  # 10 seconds
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # 1000 time points for evaluation

# Solve for small angle (15 degrees)
initial_conditions_small = [theta0, 0]  # [theta, dtheta/dt]
solution_small = solve_ivp(pendulum, t_span, initial_conditions_small, t_eval=t_eval)

# Analytical solution for small angles
analytical_solution_small = theta0 * np.cos(np.sqrt(g / L) * t_eval)

# Solve for large angle (75 degrees)
initial_conditions_large = [theta0_large, 0]  # [theta, dtheta/dt]
solution_large = solve_ivp(pendulum, t_span, initial_conditions_large, t_eval=t_eval)

# Plotting results
plt.figure(figsize=(14, 10))

# Small angle results
plt.subplot(2, 1, 1)
plt.plot(solution_small.t, np.degrees(solution_small.y[0]), label='Numerical Solution (Small Angle)', color='blue')
plt.plot(t_eval, np.degrees(analytical_solution_small), label='Analytical Solution (Small Angle)', color='orange', linestyle='--')
plt.title('Simple Pendulum - Small Angle Approximation (15 degrees)')
plt.xlabel('Time (s)')
plt.ylabel('Angle (degrees)')
plt.legend()
plt.grid()

# Large angle results
plt.subplot(2, 1, 2)
plt.plot(solution_large.t, np.degrees(solution_large.y[0]), label='Numerical Solution (Large Angle)', color='blue')
plt.title('Simple Pendulum - Large Angle Approximation (75 degrees)')
plt.xlabel('Time (s)')
plt.ylabel('Angle (degrees)')
plt.legend()
plt.grid()

plt.tight_layout()
plt.savefig('./pw3/data/2_a.png')

