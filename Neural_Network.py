'''
** Layer Dense Class **

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


class Activation_ReLU:

    # Forward pass
    def forward(self, inputs):
        
        # Calculate output values from inputs
        self.output = np.maximum(0, inputs)


class Activation_Softmax:

    # Forward pass
    def forward(self, inputs):

        # Get unnormalised probabilities
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))

        # Normalise them for each sample
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        
        self.output = probabilities 



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