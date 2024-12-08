import numpy as np
import matplotlib.pyplot as plt

def load_and_display_data(file_path):
    """
    Loads data from a file and plots it on a 2D map.

    Parameters:
    file_path (str): Path to the dataset file.

    The dataset is expected to have columns:
    - v0 (initial speed)
    - alpha (angle of throw)
    - hit (1 if successful, 0 otherwise)
    """
    # Load the dataset
    data = np.loadtxt(file_path, delimiter=';')

    # Extract features and labels
    v0 = data[:, 0]  # Initial speed
    alpha = data[:, 1]  # Angle
    hit = data[:, 2]  # Hit or miss (1 or 0)

    # Visualize the data
    plt.figure(figsize=(8, 6))
    plt.scatter(v0[hit == 1], alpha[hit == 1], color='green', label='Hit', alpha=0.7)
    plt.scatter(v0[hit == 0], alpha[hit == 0], color='red', label='Miss', alpha=0.7)
    plt.title('Basketball Free Throw Data')
    plt.xlabel('Initial Speed (v0)')
    plt.ylabel('Throw Angle (alpha)')
    plt.legend()
    plt.grid()
    plt.show()

# Example usage
load_and_display_data("learningDataSetIdeal.csv")  # Replace with your actual file path
