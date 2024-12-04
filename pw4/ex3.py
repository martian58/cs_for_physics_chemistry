"""
3. Using linear scipy.optimize
    a. Write a function that takes the vector 𝐱 = 𝑉𝐴, 𝑉𝐵, 𝑉𝐶, 𝑉𝐷 as well as 𝑉𝐶𝐶, 𝑅1, 𝑅2, 𝑅3 and 𝑅4
    as arguments and that calculate the cost function associated with our system

    b. Use minimize to minimize this cost function.

    c. Compare the results with ones obtained with previous methods
"""

import numpy as np
from scipy.optimize import minimize



class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Step 3a: Define the cost function
# This function calculates the sum of squared errors (SSE) between the equations.
def cost_function(variables, Vcc, R1, R2, R3, R4):
    """
    Calculates the cost function as the sum of squared errors for the given equations.

    Args:
        variables (list): [Va, Vb, Vc, Vd] - Voltages at nodes A, B, C, and D.
        Vcc, R1, R2, R3, R4 (float): Circuit parameters (voltage and resistance values).

    Returns:
        float: Sum of squared errors of the equations, which we aim to minimize.
    """
    Va, Vb, Vc, Vd = variables  # Unpack the variables (voltages at nodes A, B, C, and D)
    
    # The system of equations (from the previous part)
    equations = [
        Va - (Vcc / R1 + Vc / R3 + Vb / R3 + Vd / R4) / (1 / R1 + 2 / R3 + 1 / R4),
        Vb - (Vcc / R2 + Vd / R3 + Va / R3) / (1 / R2 + 2 / R3),
        Vc - (Va / R3 + Vd / R3) / (1 / R3 + 2 / R3),
        Vd - (Vb / R3 + Vc / R3 + Va / R4) / (1 / R1 + 2 / R3 + 1 / R4)
    ]
    
    # Sum of squared errors of the system 
    return sum(eq**2 for eq in equations)  # Return the sum of squared errors

# Step 3b: Minimize the cost function using SciPy's `minimize`
# These are the numerical values for the voltage and resistances
Vcc_value = 15  # voltage source 
R_values = {
    "R1": 1000,  # resistance R1 
    "R2": 2000,  # resistance R2 
    "R3": 10000,  # resistance R3 
    "R4": 500,   # resistance R4 
}

# Initial guess for the variables [Va, Vb, Vc, Vd], we start with zero voltages
initial_guess = [0, 0, 0, 0]

# Use SciPy's minimize function to minimize the cost function
# We use the BFGS optimization method, which is efficient for this type of problem
result = minimize(
    cost_function,
    initial_guess,
    args=(Vcc_value, R_values["R1"], R_values["R2"], R_values["R3"], R_values["R4"]),
    method='BFGS'
)

# Step 3c: Extract the minimized solution from the result
# This gives us the optimized values for Va, Vb, Vc, and Vd
solution_minimization = result.x

# Print the results from the optimization process
print(f"\n{Colors.HEADER}{Colors.BOLD}Task 3b: Optimization Result{Colors.END}")
print(f"{Colors.UNDERLINE}Success: {result.success}, Message: {result.message}{Colors.END}")

# Print the solution obtained after minimization
print(f"\n{Colors.HEADER}{Colors.BOLD}Task 3c: Solution using Cost Function Minimization{Colors.END}")
print(f"{Colors.UNDERLINE}The minimized solution for Va, Vb, Vc, and Vd is:{Colors.END}")
print(f"{Colors.GREEN}Va = {solution_minimization[0]:.4f} V{Colors.END}")
print(f"{Colors.GREEN}Vb = {solution_minimization[1]:.4f} V{Colors.END}")
print(f"{Colors.GREEN}Vc = {solution_minimization[2]:.4f} V{Colors.END}")
print(f"{Colors.GREEN}Vd = {solution_minimization[3]:.4f} V{Colors.END}")
