from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np

def knn_classifier(train_file, test_file, n_neighbors=5):
    """
    Trains and evaluates a K-Nearest Neighbors classifier.

    Parameters:
    train_file (str): Path to the training dataset file.
    test_file (str): Path to the testing dataset file.
    n_neighbors (int): Number of neighbors for KNN.

    The function prints confusion matrices and accuracy scores.
    """
    # Load datasets
    train_data = np.loadtxt(train_file, delimiter=';')
    test_data = np.loadtxt(test_file, delimiter=';')

    # Split features and labels
    X_train, y_train = train_data[:, :2], train_data[:, 2]
    X_test, y_test = test_data[:, :2], test_data[:, 2]

    # Train the KNN model
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(X_train, y_train)

    # Make predictions
    train_preds = knn.predict(X_train)
    test_preds = knn.predict(X_test)

    # Evaluate the model
    print(f"Training Accuracy: {accuracy_score(y_train, train_preds):.2f}")
    print(f"Testing Accuracy: {accuracy_score(y_test, test_preds):.2f}")

    print("\nConfusion Matrix (Training Data):")
    print(confusion_matrix(y_train, train_preds))

    print("\nConfusion Matrix (Testing Data):")
    print(confusion_matrix(y_test, test_preds))

# Example usage
knn_classifier("learningDataSetIdeal.csv", "verifDataSetIdeal.csv", n_neighbors=3)
