from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import numpy as np

def decision_tree_classifier(train_file, test_file, max_depth=None):
    """
    Trains and evaluates a Decision Tree classifier.

    Parameters:
    train_file (str): Path to the training dataset file.
    test_file (str): Path to the testing dataset file.
    max_depth (int): Maximum depth of the decision tree. Default is None (no limit).
    """
    train_data = np.loadtxt(train_file, delimiter=';')
    test_data = np.loadtxt(test_file, delimiter=';')

    X_train, y_train = train_data[:, :2], train_data[:, 2]
    X_test, y_test = test_data[:, :2], test_data[:, 2]

    # Train the Decision Tree model
    dt = DecisionTreeClassifier(max_depth=max_depth)
    dt.fit(X_train, y_train)

    # Evaluate the model
    print(f"Training Accuracy: {dt.score(X_train, y_train):.2f}")
    print(f"Testing Accuracy: {dt.score(X_test, y_test):.2f}")

    # Visualize the decision tree
    plt.figure(figsize=(12, 8))
    plot_tree(dt, filled=True, feature_names=['v0', 'alpha'], class_names=['Miss', 'Hit'])
    plt.title("Decision Tree Visualization")
    plt.show()

# Example usage
decision_tree_classifier("learningDataSetIdeal.csv", "verifDataSetIdeal.csv", max_depth=3)
