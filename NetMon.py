import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class NeuralNetworkVisualizer:
    def __init__(self):
        self.training_history = {'epoch': [], 'loss': [], 'accuracy': []}

    def update_training_history(self, epoch, loss, accuracy):
        self.training_history['epoch'].append(epoch)
        self.training_history['loss'].append(loss)
        self.training_history['accuracy'].append(accuracy)

    def plot_training_history(self):
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.plot(self.training_history['epoch'], self.training_history['loss'], label='Loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.plot(self.training_history['epoch'], self.training_history['accuracy'], label='Accuracy')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.legend()

        plt.tight_layout()
        plt.show()

    def plot_data_distribution(self, data, title):
        # Assuming data is a NumPy array or DataFrame
        plt.figure(figsize=(8, 6))
        plt.hist(data, bins=30)
        plt.title(title)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.show()

# Example usage:
if __name__ == "__main__":
    visualizer = NeuralNetworkVisualizer()

    # Simulate training process and update the history
    for epoch in range(1, 11):
        loss = np.random.rand() * 2  # Random loss value for demonstration
        accuracy = 0.5 + np.random.rand() * 0.5  # Random accuracy value for demonstration
        visualizer.update_training_history(epoch, loss, accuracy)

    # Plot training history
    visualizer.plot_training_history()

    # Simulate data distribution
    data = np.random.randn(1000)  # Random data for demonstration
    visualizer.plot_data_distribution(data, title='Data Distribution')
