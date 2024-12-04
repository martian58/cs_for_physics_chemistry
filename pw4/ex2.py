"""
2. Using Linear Algebra
    a. Assuming that x = VA, VB, VC, VD, calculate the matrix A and the vector B.
    b. Use numpy.linalg or sympy.linalg to define the matrix A and the vector B.
    c. Calculate A^-1.
    d. Calculate the product A^-1 * B with VCC = 15V, R1 = 1000Ω, R2 = 2000Ω, R3 = 10000Ω, and R4 = 500Ω.
    e. Use directly linalg.solve with A and B as a parameter and compare the results.
"""

import numpy as np


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

"""
* Step 2a: Define the numerical parameters for the problem
* We have the following values:
* Vcc = 15V (voltage source) and resistor values for R1, R2, R3, and R4.
"""

Vcc_value = 15  # Voltage source
R_values = {
    "R1": 1000,  # Resistance R1 
    "R2": 2000,  # Resistance R2 
    "R3": 10000,  # Resistance R3 
    "R4": 500,   # Resistance R4 
}

# Step 2b: Construct the coefficient matrix A and the vector B
# These represent the system of equations in matrix form: A * x = B
A = np.array([
    [1, -1/(2*R_values["R3"]), -1/R_values["R3"], -1/R_values["R4"]],
    [-1/(2*R_values["R3"]), 1, -1/(2*R_values["R3"]), 0],
    [-1/R_values["R3"], -1/(2*R_values["R3"]), 1, -1/(2*R_values["R3"])],
    [-1/R_values["R4"], 0, -1/(2*R_values["R3"]), 1]
], dtype=float)

# Vector B is based on the right-hand side of the equations.
# Here, we include the values for the voltage sources.
B = np.array([
    Vcc_value / R_values["R1"],  # Current source for node A
    Vcc_value / R_values["R2"],  # Current source for node B
    0,  # No current source for node C
    0   # No current source for node D
], dtype=float)

# Step 2c: Compute the inverse of matrix A (A^-1)
# We will need this for later in Step 2d.
A_inv = np.linalg.inv(A)  # Calculate the inverse of A

# Step 2d: Calculate the product A^-1 * B to solve for the voltages (Va, Vb, Vc, Vd)
# This is equivalent to solving for the node voltages.
solution_manual = np.dot(A_inv, B)

# Step 2e: Use NumPy's direct solver to find the solution to A * x = B
# This is a more straightforward approach and should yield the same results.
solution_direct = np.linalg.solve(A, B)

# Print the results for each part
print(f"\n{Colors.HEADER}{Colors.BOLD}Task 2c: Inverse of Matrix A{Colors.END}")
print(f"{Colors.UNDERLINE}The inverse of matrix A is:{Colors.END}")
print(A_inv)

print(f"\n{Colors.HEADER}{Colors.BOLD}Task 2d: Solution using A^-1 * B{Colors.END}")
print(f"{Colors.UNDERLINE}The solution for Va, Vb, Vc, and Vd is:{Colors.END}")
print(f"{Colors.GREEN}Va = {solution_manual[0]:.4f} V{Colors.END}")
print(f"{Colors.GREEN}Vb = {solution_manual[1]:.4f} V{Colors.END}")
print(f"{Colors.GREEN}Vc = {solution_manual[2]:.4f} V{Colors.END}")
print(f"{Colors.GREEN}Vd = {solution_manual[3]:.4f} V{Colors.END}")

print(f"\n{Colors.HEADER}{Colors.BOLD}Task 2e: Solution using NumPy's direct solver{Colors.END}")
print(f"{Colors.UNDERLINE}The solution for Va, Vb, Vc, and Vd using NumPy's solver is:{Colors.END}")
print(f"{Colors.GREEN}Va = {solution_direct[0]:.4f} V{Colors.END}")
print(f"{Colors.GREEN}Vb = {solution_direct[1]:.4f} V{Colors.END}")
print(f"{Colors.GREEN}Vc = {solution_direct[2]:.4f} V{Colors.END}")
print(f"{Colors.GREEN}Vd = {solution_direct[3]:.4f} V{Colors.END}")