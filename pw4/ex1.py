"""
Task 1: Formal Computation

    a. Use sympy.symbols and sympy.solve to obtain the analytic equations of VA, VB, VC,
       VD as a function of VCC, R1, R2, R3, and R4.

    b. Use the subs() method to calculate the numerical value of VA, VB, VC, VD for 
       VCC = 15, R1 = 1000Ω, R2 = 2000Ω, R3 = 10000Ω, and R4 = 500Ω.

Author: Fuad Alizada
Date:   2024-11-18
"""

import sympy as sp

# ANSI for colorful prints :)
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
* Step 1a: Define the problem parameters and equations
*-----------------------------------------------------
* Vcc <-> voltage source to the circuit.
* R1, R2, R3, R4 <-> resistor value.
* Va, Vb, Vc, Vd <-> voltages we aim to calculate.
"""
Vcc, R1, R2, R3, R4 = sp.symbols('Vcc R1 R2 R3 R4')
Va, Vb, Vc, Vd = sp.symbols('Va Vb Vc Vd')

"""
* The equations are found using Millmann's theorem, which states that each of the voltage sources and 
  their respective resistors produce a current, and the sum of all currents is equal to the total current produced by the circuit.

 Source --> https://www.oreilly.com/library/view/introductory-electrical-engineering/9781119580188/c24.xhtml

* Each equation is for  one of the nodes in the circuit:
*   eq1 <-> Voltage at A (Va).
*   eq2 <-> Voltage at  B (Vb).
*   eq3 <-> Voltage at  C (Vc).
*   eq4 <-> Voltage at  D (Vd).
"""

# Equation for  A
eq1 = sp.Eq(Va, (Vcc/R1 + Vc/R3 + Vb/R3 + Vd/R4) / (1/R1 + 2/R3 + 1/R4))

# Equation for  B
eq2 = sp.Eq(Vb, (Vcc/R2 + Vd/R3 + Va/R3) / (1/R2 + 2/R3))

# Equation for  C
eq3 = sp.Eq(Vc, (Va/R3 + Vd/R3) / (1/R3 + 2/R3))

# Equation for node D
eq4 = sp.Eq(Vd, (Vb/R3 + Vc/R3 + Va/R4) / (1/R1 + 2/R3 + 1/R4))

"""
* Step 1b: Solve the equations symbolically
* -----------------------------------------------------
* Here we use sympy's solve function to compute the symbolic solutions for Va, Vb, Vc, Vd.
"""
solution = sp.solve([eq1, eq2, eq3, eq4], [Va, Vb, Vc, Vd])

# Display the symbolic solution
print(f"{Colors.HEADER}{Colors.BOLD}Task 1b: Formal Symbolic Solution{Colors.END}")
print(f"{Colors.UNDERLINE}The solutions for Va, Vb, Vc, and Vd are:{Colors.END}")
for var, expr in solution.items():
    print(f"{Colors.BLUE}{var} = {expr}{Colors.END}")

"""
* Step 1c: Substitute numerical values into the symbolic solution
* -----------------------------------------------------
* We substitute specific numerical values for Vcc, R1, R2, R3, and R4 into the symbolic solution.
* These values represent a specific configuration of the circuit:
*   - Vcc = 15V (voltage source)
*   - R1 = 1000Ω, R2 = 2000Ω, R3 = 10000Ω, R4 = 500Ω (resistor values)
""" 
values = {Vcc: 15, R1: 1000, R2: 2000, R3: 10000, R4: 500}

# Compute the numerical solution by evaluating the symbolic solution with the given values
numerical_solution = {k: v.evalf(subs=values) for k, v in solution.items()}

# Display the numerical solution
print(f"\n{Colors.HEADER}{Colors.BOLD}Task 1c: Numerical Solution (Sympy){Colors.END}")
print(f"{Colors.UNDERLINE}The numerical solutions for Va, Vb, Vc, and Vd are:{Colors.END}")
for var, val in numerical_solution.items():
    print(f"{Colors.GREEN}{var} = {val:.4f} V{Colors.END}")