import numpy as np
from scipy.optimize import curve_fit

# Fluorescence lifetimes for the molecules (in ns)
LIFETIMES = [200.9, 5.8, 38.6, 516.2, 57.8, 8.9]

def import_text_data_with_time(file_path, time_start=0, time_stop=1000, time_step=0.2):
    """
    Import fluorescence signal data from a text file and generate corresponding time values.

    Parameters:
        file_path (str): Path to the text file.
        time_start (float): Start time in ns.
        time_stop (float): Stop time in ns.
        time_step (float): Time step in ns.

    Returns:
        tuple: Time (numpy array) and signal (numpy array).
    """
    # Generate time values
    time = np.arange(time_start, time_stop + time_step, time_step)
    # Load signal values
    signal = np.loadtxt(file_path)

    if len(signal) != len(time):
        raise ValueError("Mismatch between signal length and generated time points.")
    return time, signal

def multi_exponential_decay(t, *params):
    """
    Multi-component exponential decay function.

    Parameters:
        t (numpy.ndarray): Time values.
        params (tuple): Alternating amplitudes (A) and lifetimes (tau).

    Returns:
        numpy.ndarray: Fluorescence signal.
    """
    signal = np.zeros_like(t)
    for i in range(0, len(params), 2):
        A = params[i]
        tau = params[i + 1]
        signal += A * np.exp(-t / tau)
    return signal

def fit_mixture(file_path, lifetimes, components):
    """
    Fit fluorescence data for a mixture of PAHs.

    Parameters:
        file_path (str): Path to the text file containing fluorescence data.
        lifetimes (list): Predefined lifetimes of PAHs.
        components (int): Number of PAHs in the mixture.

    Returns:
        dict: Fitted amplitudes and lifetimes for each component.
    """
    # Load data
    time, signal = import_text_data_with_time(file_path)

    # Initial guesses: equal amplitudes and known lifetimes
    initial_guess = []
    bounds_lower, bounds_upper = [], []
    for i in range(components):
        initial_guess.extend([1.0, lifetimes[i]])  # Guess: A=1.0, tau=lifetime
        bounds_lower.extend([0, lifetimes[i] * 0.8])  # Amplitude >= 0, lifetime ±20%
        bounds_upper.extend([np.inf, lifetimes[i] * 1.2])

    # Curve fitting
    params, _ = curve_fit(
        multi_exponential_decay, time, signal, p0=initial_guess, bounds=(bounds_lower, bounds_upper)
    )

    # Group parameters into amplitude-lifetime pairs
    result = {
        f"Component {i+1}": {"Amplitude (A)": params[2 * i], "Lifetime (tau)": params[2 * i + 1]}
        for i in range(components)
    }
    return result
# Fit Mixture A (Data1.txt, 1 PAH)
result_a = fit_mixture('Data1.txt', LIFETIMES, components=1)
print("Mixture A Results:", result_a)

# Fit Mixture B (Data2.txt, 2 PAHs)
result_b = fit_mixture('Data2.txt', LIFETIMES, components=2)
print("Mixture B Results:", result_b)

# Fit Mixture C (Data3.txt, 3 PAHs)
result_c = fit_mixture('Data3.txt', LIFETIMES, components=3)
print("Mixture C Results:", result_c)
