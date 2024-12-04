import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def gillespie_enzymatic_reaction(k1: float, km1: float, k2: float, 
                                 E0: int, S0: int, ES0: int, P0: int,
                                 t_max: float):
    """
    This function simulates an enzymatic reaction using Gillespie's algorithm.

    The reaction involves:
        E + S ↔ ES (reversible, rates k1 and km1)
        ES → E + P (irreversible, rate k2)

    Parameters:
    - k1 (float): Forward reaction rate constant for E + S → ES.
    - km1 (float): Reverse reaction rate constant for ES → E + S.
    - k2 (float): Reaction rate constant for ES → E + P.
    - E0 (int): Initial count of enzyme E.
    - S0 (int): Initial count of substrate S.
    - ES0 (int): Initial count of enzyme-substrate complex ES.
    - P0 (int): Initial count of product P.
    - t_max (float): Total simulation time in seconds.

    Returns:
    - result (dict): A dictionary containing:
        - "time": List of time points at which reactions occurred.
        - "E", "S", "ES", "P": Lists of molecule counts over time.
    """
    E, S, ES, P = E0, S0, ES0, P0
    time = 0
    
    result = {
        "time": [time],
        "E": [E],
        "S": [S],
        "ES": [ES],
        "P": [P]
    }
    
    # Simulation loop
    while time < t_max:
        r1 = k1 * E * S        # E + S -> ES
        r2 = km1 * ES          # ES -> E + S
        r3 = k2 * ES           # ES -> E + P
        total_rate = r1 + r2 + r3
        
        # If no reactions can occur, then can exit the loop
        if total_rate == 0:
            break
        
        # Determine time until the next reaction
        time += np.random.exponential(1 / total_rate)
        
        # Choose which reaction occurs
        rand = np.random.rand()
        if rand < r1 / total_rate:
            # Reaction: E + S -> ES
            E -= 1
            S -= 1
            ES += 1
        elif rand < (r1 + r2) / total_rate:
            # Reaction: ES -> E + S
            E += 1
            S += 1
            ES -= 1
        else:
            # Reaction: ES -> E + P
            ES -= 1
            E += 1
            P += 1
        
        # Record the updated state and time
        result["time"].append(time)
        result["E"].append(E)
        result["S"].append(S)
        result["ES"].append(ES)
        result["P"].append(P)
    
    return result

def deterministic_enzymatic_reaction(y, t, k1, km1, k2):
    """
    Defines the system of ODEs for the enzymatic reaction.

    Parameters:
    - y (list): List of current concentrations [E, S, ES, P].
    - t (float): Current time.
    - k1, km1, k2 (float): Reaction rate constants.

    Returns:
    - dydt (list): Derivatives [dE/dt, dS/dt, dES/dt, dP/dt].
    """
    E, S, ES, P = y
    dE = -k1 * E * S + km1 * ES + k2 * ES
    dS = -k1 * E * S + km1 * ES
    dES = k1 * E * S - km1 * ES - k2 * ES
    dP = k2 * ES
    return [dE, dS, dES, dP]

# Constants and initial conditions
k1 = 1.0
km1 = 0.01
k2 = 5.0
E0 = 10
S0 = 200
ES0 = 0
P0 = 0
t_max = 5.0

# Run Gillespie's algorithm
gillespie_result = gillespie_enzymatic_reaction(k1, km1, k2, E0, S0, ES0, P0, t_max)

# Deterministic simulation using odeint
y0 = [E0, S0, ES0, P0]
time_points = np.linspace(0, t_max, 100)
deterministic_result = odeint(deterministic_enzymatic_reaction, y0, time_points, args=(k1, km1, k2))

# Plot results
plt.figure(figsize=(12, 8))

# Gillespie's algorithm results
plt.plot(gillespie_result["time"], gillespie_result["E"], 'o', label="E (Gillespie)")
plt.plot(gillespie_result["time"], gillespie_result["S"], 'o', label="S (Gillespie)")
plt.plot(gillespie_result["time"], gillespie_result["ES"], 'o', label="ES (Gillespie)")
plt.plot(gillespie_result["time"], gillespie_result["P"], 'o', label="P (Gillespie)")

# Deterministic results
plt.plot(time_points, deterministic_result[:, 0], '-', label="E (Deterministic)")
plt.plot(time_points, deterministic_result[:, 1], '-', label="S (Deterministic)")
plt.plot(time_points, deterministic_result[:, 2], '-', label="ES (Deterministic)")
plt.plot(time_points, deterministic_result[:, 3], '-', label="P (Deterministic)")

plt.xlabel("Time (s)")
plt.ylabel("Molecule Count")
plt.legend()
plt.title("Gillespie's Algorithm vs Deterministic Model")
plt.grid()
plt.show()
