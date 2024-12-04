import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import os

os.makedirs('./pw3/data', exist_ok=True)
# Define parameters
R = 1000  # Resistance in ohms
C = 1e-9  # Capacitance in farads
Vin = 5.0  # Input voltage in volts
t_span = (0, 10e-6)  # Time span for simulation (0 to 10 microseconds)
t_eval = np.linspace(t_span[0], t_span[1], 100)  # 100 time points for evaluation

# Define the differential equation
def rc_circuit(t, V_C):
    return (Vin / (R * C)) - V_C

# Solve the differential equation numerically
sol = solve_ivp(rc_circuit, t_span, [0], t_eval=t_eval)

# Compute the analytic solution
analytic_solution = Vin * (1 - np.exp(-t_eval / (R * C)))

# Calculate the relative difference
relative_difference = np.zeros_like(sol.t)  # Initialize with zeros
non_zero_analytic = analytic_solution != 0  # Mask for non-zero values

# Avoid division by zero for relative difference
relative_difference[non_zero_analytic] = np.abs((sol.y[0][non_zero_analytic] - analytic_solution[non_zero_analytic]) / analytic_solution[non_zero_analytic]) * 100

# Plotting the results
plt.figure(figsize=(12, 8))

# Plot numerical and analytic solutions
plt.subplot(2, 1, 1)
plt.plot(sol.t, sol.y[0], label='Numerical Solution', color='blue')
plt.plot(t_eval, analytic_solution, label='Analytic Solution', color='orange', linestyle='--')
plt.title('Voltage across the Capacitor')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.grid()

# Plot relative difference
plt.subplot(2, 1, 2)
plt.plot(sol.t, relative_difference, color='green')
plt.title('Relative Difference between Numerical and Analytic Solutions')
plt.xlabel('Time (s)')
plt.ylabel('Relative Difference (%)')
plt.ylim(0, np.max(relative_difference) + 5)  # Set y-limits based on max relative difference
plt.grid()

plt.tight_layout()
plt.savefig('./pw3/data/1_a.png')
