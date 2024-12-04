import numpy as np
import matplotlib.pyplot as plt

def gillespie_simple_reaction(kf: float, kr: float, A0: int, B0: int, AB0: int, t_max: float):
    """
    This function simulates a chemical reaction using Gillespie's algorithm.

    The chemical system involves three species: A, B, and AB with the reactions:
        A + B -> AB with a forward reaction rate kf * A * B
        AB -> A + B with a reverse reaction rate kr * AB

    Parameters:
    - kf (float): Forward reaction rate constant.
    - kr (float): Reverse reaction rate constant.
    - A0 (int): Initial count of species A.
    - B0 (int): Initial count of species B.
    - AB0 (int): Initial count of species AB.
    - t_max (float): Total simulation time in seconds.

    Returns:
    - result (dict): A dictionary containing:
        - "time": List of time points at which reactions occurred.
        - "A": List of molecule counts for species A over time.
        - "B": List of molecule counts for species B over time.
        - "AB": List of molecule counts for species AB over time.
    """

    A, B, AB = A0, B0, AB0
    time = 0
    
    result = {
        "time": [time],  # Initial time (0)
        "A": [A],        # Initial count of A
        "B": [B],        # Initial count of B
        "AB": [AB]       # Initial count of AB
    }
    
    while time < t_max:
        r1 = kf * A * B  # Rate of forward reaction (A + B -> AB)
        r2 = kr * AB     # Rate of reverse reaction (AB -> A + B)
        total_rate = r1 + r2  # Combined reaction rate
        
        # If no reactions can occur, then exit
        if total_rate == 0:
            break
        
        time += np.random.exponential(1 / total_rate)
        
        if np.random.rand() < r1 / total_rate:
            # Forward reaction: A + B -> AB
            A -= 1  # Consume one molecule of A
            B -= 1  # Consume one molecule of B
            AB += 1 # Produce one molecule of AB
        else:
            # Reverse reaction: AB -> A + B
            A += 1  # Produce one molecule of A
            B += 1  # Produce one molecule of B
            AB -= 1 # Consume one molecule of AB
        
        result["time"].append(time)
        result["A"].append(A)
        result["B"].append(B)
        result["AB"].append(AB)
    
    return result

kf = 0.05    # Forward reaction rate constant
kr = 0.005   # Reverse reaction rate constant
A0 = 800     # Initial count of species A
B0 = 400     # Initial count of species B
AB0 = 100    # Initial count of species AB
t_max = 1.0  # Total simulation time in seconds

result = gillespie_simple_reaction(kf, kr, A0, B0, AB0, t_max)

# Plot the simulation results
plt.figure(figsize=(10, 6))
plt.plot(result["time"], result["A"], label="A (molecule count)")
plt.plot(result["time"], result["B"], label="B (molecule count)")
plt.plot(result["time"], result["AB"], label="AB (molecule count)")
plt.xlabel("Time (seconds)")
plt.ylabel("Molecule Count")
plt.legend()
plt.title("Gillespie's Algorithm - Simple Chemical Reaction")
plt.grid()
plt.show()

AB_ss = A0 * B0 * kf / (kr + kf * A0 * B0)  # Steady-state AB concentration
A_ss = A0 + AB0 - AB_ss                    # Steady-state A concentration
B_ss = B0 + AB0 - AB_ss                    # Steady-state B concentration

print("Theoretical Steady-State Values:")
print(f"A: {A_ss:.2f}, B: {B_ss:.2f}, AB: {AB_ss:.2f}")
