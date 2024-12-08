import numpy as np
import matplotlib.pyplot as plt

def display_data(file_path: str):
    """
    Loads a dataset and visualizes it on a map.

    Parameters:
    file_path (str): Path to the dataset file.

    The dataset has the following columns:
    - Column 0: Initial speed (v0)
    - Column 1: Throw angle (alpha)
    - Column 2: Hit actual (1 = Hit, 0 = Miss)
    - Column 3: Hit predicted (1 = Hit, 0 = Miss)
    """
    # Load the dataset
    data = np.loadtxt(file_path, delimiter=';')

    # Extract data columns
    v0 = data[:, 0]  # Initial speed
    alpha = data[:, 1]  # Throw angle
    actual = data[:, 2]  # Actual hit 
    predicted = data[:, 3]  # Predicted hit 

    # Set up the plot
    plt.figure(figsize=(10, 6))

    # Plot data with different markers given in the instructions
    plt.scatter(v0[(actual == 1) & (predicted == 1)], 
                alpha[(actual == 1) & (predicted == 1)], 
                c='green', label='True Positive (⚫)', marker='o')
    plt.scatter(v0[(actual == 1) & (predicted == 0)], 
                alpha[(actual == 1) & (predicted == 0)], 
                c='blue', label='False Negative (X)', marker='X')
    plt.scatter(v0[(actual == 0) & (predicted == 1)], 
                alpha[(actual == 0) & (predicted == 1)], 
                c='red', label='False Positive (X)', marker='X')
    plt.scatter(v0[(actual == 0) & (predicted == 0)], 
                alpha[(actual == 0) & (predicted == 0)], 
                c='red', label='True Negative (⚫)', marker='o')

    # Customize plot
    plt.title("Visualization of Free Throw Data")
    plt.xlabel("Initial Speed (v0)")
    plt.ylabel("Throw Angle (alpha)")
    plt.legend()
    plt.grid(True)
    plt.show()

display_data("learningDataSetIdeal.csv")
display_data("learningDataSetNoisy.csv")
display_data("verifDataSetIdeal.csv")
