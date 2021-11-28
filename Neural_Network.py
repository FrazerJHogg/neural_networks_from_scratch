'''
** Neural Network **

'''

import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()
 

class Layer_Dense:

    # Layer initialisation
    def __init__(self, n_inputs, n_neurons):
        
        # Initialise weights and biases 
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    # Forward pass
    def forward(self, inputs):
        
        # Calculate output values from inputs, weights and biases
        self.output = np.dot(inputs, self.weights) + self.biases

        # For storing inputs
        self.inputs = inputs

    # Backward pass 
    def backward(self, dvalues):
        # Gradients on parameters
        self.dweights = np.dot(self.inputs.T, dvalues)
        self.dbiases = np.sum(dvalues, axis=0, keepdims=True)

        # Gradient on values 
        self.dinputs = np.dot(dvalues, self.weights.T)


class Activation_ReLU:

    # Forward pass
    def forward(self, inputs):
        
        # Calculate output values from inputs
        self.output = np.maximum(0, inputs)

        # For storing inputs
        self.inputs = inputs
        self.output = np.maximum(0, inputs)

    # Backward pass 
    def backward(self, dvalues):
        # Since the original variable needs to be modified, 
        # this makes a copy of the values
        self.dinputs = dvalues.copy()

        # Zero gradient where input values were negative
        self.dinputs[self.inputs <= 0] = 0


class Activation_Softmax:

    # Forward pass
    def forward(self, inputs):

        # Get unnormalised probabilities
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))

        # Normalise them for each sample
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        
        self.output = probabilities 


# Common loss class
class Loss:

    # Calculate the data and regularisation losses
    # given model output and ground-truth values 
    def calculate(self, output, y):

        # Calculate sample losses 
        sample_losses = self.forward(output, y)

        # Calculate mean losses
        data_loss = np.mean(sample_losses)

        #Return loss
        return data_loss


# Cross-entropy loss
class Loss_CategoricalCrossentropy(Loss):

    # Forward pass
    def forward(self, y_pred, y_true):

        # Number of samples in a batch
        samples = len(y_pred)

        # Clip data to prevent division by 0
        # Clip both sides to not drag mean towards any value 
        y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)

        # Probabilities for taget values only
        # if categorical labels 
        if len(y_true.shape) == 1:
            correct_confidences = y_pred_clipped [
                range(samples), y_true
            ]

        # Mask values - only for one-hot encoded labels
        elif len(y_true.shape) == 2:
            correct_confidences = np.sum(
                y_pred_clipped*y_true, axis=1
            )

        # Losses
        negative_log_likelihoods = -np.log(correct_confidences)
        return negative_log_likelihoods

    # Backward pass 
    def backward(self, dvalues, y_true):

        # Number of samples 
        samples = len(dvalues)
        # Number of labels in every sample 
        # using the first samples to count them 
        labels = len(dvalues[0])

        # If lavels are sparse, turn them into one-hot vector 
        if len(y_true.shape) == 1:
            y_true = np.eye(labels)[y_true]

        # Calculate gradient
        self.dinputs = -y_true / dvalues
        # Normalise gradient 
        self.dinputs = self.dinputs / samples


# Create dataset
X, y = spiral_data (samples=100, classes=3)
 
# Creare Dense Layer with 2 input features and 3 output values 
dense1 = Layer_Dense(2, 3)

# Create ReLU activation (to be used with Dense layer)
activation1 = Activation_ReLU()

# Create a second Dense layer with 3 input features (as we take
# output of previous layer here) and 3 output values
dense2 = Layer_Dense(3, 3)

# Create Softmax activation (to de used with Dense layer)
activation2 = Activation_Softmax()

# Make a forward pass of our training data through this layer 
dense1.forward(X)

# Create loss function
loss_function = Loss_CategoricalCrossentropy()

# Make a forward pass through activation function
# it takes the out of the first Dense Layer here
activation1.forward(dense1.output)

# Make a forward pass through the second Dense Layer
# it takes the output of the first dense layer here
dense2.forward(activation1.output)

# Make a forward pass through activation function 
# it take the output of the second dense layer here 
activation2.forward(dense2.output)

# Let's see output of the first few samples: 
print(activation2.output[:5])

# Perform a forward pass through activation function 
# it takes the output of second dense layer here and 
# returns loss
loss = loss_function.calculate(activation2.output, y)

# Print loss value 
print('loss: ', loss)