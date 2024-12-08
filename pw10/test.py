
# Exercise 1

import numpy as np
import matplotlib.pyplot as plt

# Create dataset X: A normal distribution
# This generates 1000 random numbers with a mean of 1 and a standard deviation of 2
dataset_X = np.random.normal(loc=1, scale=2, size=1000)

# Create dataset Y: A uniform distribution
# This generates 1000 random numbers evenlyy spread between -1 and 1
dataset_Y = np.random.uniform(low=-1, high=1, size=1000)

# Create dataset Z: An exponential distribution
# This generates 1000 random numbers with an exponential distribution with an average of 5
# The `scale` parameter represents the mean for the exponential distribution
dataset_Z = np.random.exponential(scale=5, size=1000)

# Let's plot histograms to visualize the distributions of these datasets
plt.figure(figsize=(12, 6))  # Size of the figure

# Plot for dataset X
plt.subplot(1, 3, 1)  # This creates the first subplot in a 1-row, 3-column layout
plt.hist(dataset_X, bins=30, color='blue', alpha=0.7, label='Normal')  # Plot the histogram with 30 bins
plt.title('Histogram of Dataset X')  # Title of the plot
plt.xlabel('Value')  # Label for the x-axis
plt.ylabel('Frequency')  # Label for the y-axis
plt.legend()  # Add a legend for clarity

# Plot for dataset Y
plt.subplot(1, 3, 2)  # Second subplot in the same layout
plt.hist(dataset_Y, bins=30, color='green', alpha=0.7, label='Uniform')  # Uniform distribution plot
plt.title('Histogram of Dataset Y')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

# Plot for dataset Z
plt.subplot(1, 3, 3)  # Third and final subplot
plt.hist(dataset_Z, bins=30, color='red', alpha=0.7, label='Exponential')  # Exponential distribution plot
plt.title('Histogram of Dataset Z')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

plt.tight_layout()  # To prevent plots from overlap
plt.show()  # Show the plots


# Exercise 2

from scipy.stats import shapiro, probplot

def analyze_dataset(dataset: np.ndarray, label: str):
    """
    This function performs statistical analysis and visualization for a dataset.

    This function calculates the mean and standard deviation of a dataset, 
    performs the Shapiro-Wilk test to check for normality, and creates two plots:
    a histogram to visualize the frequency distribution and a Q-Q plot to compare 
    the dataset against a normal distribution.

    Parameters:
        dataset (numpy.ndarray): The dataset to be analyzed.
        label (str): A label for the dataset, used for print statements and plot titles.

    Returns:
        None: This function prints analysis results and displays plots, No return value.
    """
    print(f"\n--- Analysis of {label} ---")
    
    # Calculate mean and standard deviation of the dataset
    mean = np.mean(dataset)
    std_dev = np.std(dataset)
    print(f"Mean: {mean:.3f}")  # Print the mean value rounded to 3 decimal places (.3f)
    print(f"Standard Deviation: {std_dev:.3f}")  # Print for Standard Deaviation
    
    # Perform Shapiro-Wilk test to check for normality
    # The test returns a W-statistic and a p-value
    # If the p-value < 0.05, the data is NOT normally distributed
    stat, p_value = shapiro(dataset)
    print(f"Shapiro-Wilk Test: W-statistic = {stat:.3f}, p-value = {p_value:.3e}")
    if p_value < 0.05:
        print(f"{label} does NOT follow a normal distribution (p < 0.05).")
    else:
        print(f"{label} follow a normal distribution (p >= 0.05).")
    
    # Plot histogram to show the frequency distribution of the dataset
    plt.figure(figsize=(10, 4))  # Set figure size
    plt.subplot(1, 2, 1)  # Create a grid of plots, and use the first plot
    plt.hist(dataset, bins=30, color='gray', alpha=0.7, label=label)  # Plot histogram with 30 bins
    plt.title(f"Histogram of {label}")  # Title
    plt.xlabel("Value")  # Label for the x-axis
    plt.ylabel("Frequency")  # Label for the y axis
    plt.legend()  # Add a legend to identify the dataset
    
    # Plot Q-Q plot to compare the dataset against a normal distribution
    # Q-Q plots are used to check how similar the data is to a theoretical distribution
    plt.subplot(1, 2, 2)  # Use the second plot in the grid
    probplot(dataset, dist="norm", plot=plt)  # Generate Q-Q plot against a normal distribution
    plt.title(f"Q-Q Plot of {label}")  # Title for the Q-Q plot
    plt.tight_layout()  # Prevent overlapping
    plt.show()  # Show the plots

# Analyze dataset X (Normal distribution)
analyze_dataset(dataset_X, "Dataset X (Normal)")

# Analyze dataset Y (Uniform distribution)
analyze_dataset(dataset_Y, "Dataset Y (Uniform)")

# Analyze dataset Z (Exponential distribution)
analyze_dataset(dataset_Z, "Dataset Z (Exponential)")


# Exercise 3

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import shapiro, probplot

# Load datasets from files
ph_data = np.loadtxt("pH.txt")  # Measurements of pH from multiple experiments
cosmic_particle_data = np.loadtxt("cosmicParticle.txt")  # Timestamps of cosmic particle emissions
wind_data = np.loadtxt("wind.txt")  # Daily wind speeds recorded over a year
spinning_top_data = np.loadtxt("spinningTop.txt")  # Angles at which spinning tops stop

# Preprocess the cosmic particle data
# We need the time gaps between consecutive events, so we calculate the differences
cosmic_particle_intervals = np.diff(cosmic_particle_data)

def analyze_actual_dataset(dataset: np.ndarray, label: str):
    """
    This function analyze and visualizes a dataset.

    This function looks at a dataset and gives you the average value (mean) 
    and how spread out the data is (standard deviation). It also checks if the data fits a normal 
    distribution using a Shapiro-Wilk test, then creates two visuals:
    
    - A histogram to show the distribution of values.
    - A Q-Q plot to compare the dataset with a theoretical normal distribution.

    Parameters:
        dataset (numpy.ndarray): The data you want to analyze (e.g., pH levels, wind speeds).
        label (str): A name for the dataset, used in printouts and plot titles.

    Returns:
        None: The function doesn’t return anything but prints the analysis results and shows the plots.
    """
    print(f"\n--- Analysis of {label} ---")
    
    # Calculate and print the mean and standard deviation
    mean = np.mean(dataset)
    std_dev = np.std(dataset)
    print(f"Mean: {mean:.3f}")  # Round to 3 decimal place
    print(f"Standard Deviation: {std_dev:.3f}")
    
    # Perform the Shapiro-Wilk test to check if the data is  normally distributed
    # The test gives a W-statistic and a p-value.
    # If the p-value is less than 0.05, the data isn't normal.
    stat, p_value = shapiro(dataset)
    print(f"Shapiro-Wilk Test: W-statistic = {stat:.3f}, p-value = {p_value:.3e}")
    if p_value < 0.05:
        print(f"{label} does NOT follow a normal distribution (p < 0.05).")
    else:
        print(f"{label} follow a normal distribution (p >= 0.05).")
    
    # Plot a histogram to show how the values are distributed
    plt.figure(figsize=(10, 4))  # Make the plots a bit bigger for clarity
    plt.subplot(1, 2, 1)  # First plot in a 1-row, 2-column grid
    plt.hist(dataset, bins=30, color='purple', alpha=0.7, label=label)
    plt.title(f"Histogram of {label}")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.legend()

    # Plot a Q-Q plot to see how well the data fits a normal distribution
    plt.subplot(1, 2, 2)  # Second plot in the same grid
    probplot(dataset, dist="norm", plot=plt)  # Compare the dataset with a normal distribution
    plt.title(f"Q-Q Plot of {label}")
    plt.tight_layout()  # Adjust the layout so nothing overlaps
    plt.show()  # Display the plots

# Analyze each dataset one by one
analyze_actual_dataset(ph_data, "pH Measurements")  # Dataset of pH values
analyze_actual_dataset(cosmic_particle_intervals, "Cosmic Particle Intervals")  # Time gaps between events
analyze_actual_dataset(wind_data, "Wind Velocity")  # Wind speeds over a year
analyze_actual_dataset(spinning_top_data, "Spinning Top Angles")  # Angles of spinning tops at rest
